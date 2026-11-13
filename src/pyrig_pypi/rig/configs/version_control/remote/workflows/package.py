"""Reusable workflow for building and publishing a Python package."""

from collections.abc import Callable
from types import MethodType
from typing import Any, override

from pyrig.rig.configs.base.workflow import WorkflowConfigFile

from pyrig_pypi.rig.tools.packages.manager import PackageManager


class PackageWorkflowConfigFile(WorkflowConfigFile):
    """Build distributions and publish them to PyPI."""

    @override
    def concurrency_cancel_in_progress(self) -> bool:
        """Return `False`; package publishing must not be cancelled."""
        return False

    @override
    def jobs(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Return the package build and publish jobs."""
        return (self.job_build, self.job_publish)

    @override
    def workflow_triggers(self) -> dict[str, Any]:
        """Return a reusable-workflow trigger."""
        return self.on_workflow_call()

    @override
    def stem(self) -> str:
        """Return the workflow file stem, `package`."""
        return "package"

    def job_publish(self) -> dict[str, Any]:
        """Publish the distributions after the build succeeds."""
        return self.job(
            self.job_publish,
            needs=self.job_publish_needs(),
            environment=self.stem(),
            permissions=self.permissions_job_publish(),
            steps=self.steps_publish(),
            timeout_minutes=30,
        )

    def job_publish_needs(self) -> tuple[MethodType, ...]:
        """Return the package build prerequisite."""
        return (self.job_build,)

    def permissions_job_publish(self) -> dict[str, str]:
        """Return the OIDC permission for PyPI trusted publishing."""
        return self.permission_id_token(write=True)

    def steps_publish(self) -> list[dict[str, Any]]:
        """Return package-manager setup, artifact download, and publish steps."""
        setup_package_manager = self.step_setup_package_manager()
        setup_package_manager["with"]["enable-cache"] = "false"
        return [
            setup_package_manager,
            self.step_download_distributions(),
            self.step_publish_package(),
        ]

    def job_build(self) -> dict[str, Any]:
        """Build and upload distributions."""
        return self.job(
            self.job_build,
            permissions=self.permissions_job_build(),
            steps=self.steps_build(),
            timeout_minutes=60,
        )

    def step_download_distributions(self) -> dict[str, Any]:
        """Download the distributions into the package directory."""
        return self.step_download_artifact(
            self.step_download_distributions,
            name=self.distributions_artifact_name(),
            path=PackageManager.I.dist_dir(),
        )

    def step_publish_package(self) -> dict[str, Any]:
        """Publish the distributions using PyPI trusted publishing."""
        return self.step(
            self.step_publish_package,
            run=str(PackageManager.I.publish_trusted_args()),
        )

    def permissions_job_build(self) -> dict[str, str]:
        """Return read-only repository permissions for checkout."""
        return self.permission_contents()

    def steps_build(self) -> list[dict[str, Any]]:
        """Return setup, package build, and artifact upload steps."""
        return [
            *self.steps_core_setup(),
            self.step_build_package(),
            self.step_upload_distributions(),
        ]

    def step_build_package(self) -> dict[str, Any]:
        """Build wheel and source distributions."""
        return self.step(
            self.step_build_package,
            run=str(PackageManager.I.build_args()),
        )

    def step_upload_distributions(self) -> dict[str, Any]:
        """Upload the distributions as a workflow artifact."""
        return self.step_upload_artifact(
            self.step_upload_distributions,
            name=self.distributions_artifact_name(),
            path=PackageManager.I.dist_dir(),
        )

    def distributions_artifact_name(self) -> str:
        """Return the shared workflow-artifact name for distributions."""
        return "distributions"

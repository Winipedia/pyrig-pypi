"""Deploy workflow extended to build the package and publish it to PyPI."""

from collections.abc import Callable
from types import MethodType
from typing import Any, override

from pyrig.rig.configs.pyproject import PyprojectConfigFile
from pyrig.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)

from pyrig_pypi.rig.tools.packages.manager import PackageManager


class DeployWorkflowConfigFile(BaseDeployWorkflowConfigFile):
    """Deploy workflow that builds a package and publishes it to PyPI."""

    @override
    def jobs(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Return the workflow's job builders, adding package build and publish.

        Returns:
            Tuple of base job builders plus the package build and publish builders.
        """
        return (
            *super().jobs(),
            self.job_build_package,
            self.job_publish_package,
        )

    def job_publish_package(self) -> dict[str, Any]:
        """Build the job that publishes the uploaded distributions to PyPI.

        Returns:
            Job configuration for publishing the package distributions.
        """
        return self.job(
            self.job_publish_package,
            needs=self.job_publish_package_needs(),
            environment="package",
            permissions=self.job_publish_package_permissions(),
            steps=self.steps_publish_package(),
            timeout_minutes=30,
        )

    def job_publish_package_needs(self) -> tuple[MethodType, ...]:
        """Return the package build prerequisite for publishing.

        Returns:
            Tuple containing the package build job.
        """
        return (self.job_build_package,)

    def job_publish_package_permissions(self) -> dict[str, Any]:
        """Return the OIDC permission required for PyPI trusted publishing.

        Returns:
            Permissions mapping granting `id-token: write`.
        """
        return self.permission_id_token(write=True)

    def steps_publish_package(self) -> list[dict[str, Any]]:
        """Build the ordered steps for publishing distributions to PyPI.

        Returns:
            Package-manager setup, artifact download, and publish steps.
        """
        python_version = str(
            PyprojectConfigFile.I.latest_possible_python_version(level="minor"),
        )
        return [
            self.step_setup_package_manager(python_version=python_version),
            self.step_download_package_distributions(),
            self.step_publish_package(),
        ]

    def job_build_package(self) -> dict[str, Any]:
        """Build the job that creates and uploads the package distributions.

        Returns:
            Job configuration for building and storing the package distributions.
        """
        return self.job(
            self.job_build_package,
            permissions=self.job_build_package_permissions(),
            steps=self.steps_build_package(),
            timeout_minutes=60,
        )

    def step_download_package_distributions(self) -> dict[str, Any]:
        """Build a step that downloads distributions into the `dist/` directory.

        Returns:
            Step using `actions/download-artifact`.
        """
        return self.step_download_artifact(
            self.step_download_package_distributions,
            name=self.package_artifact_name(),
            path=PackageManager.I.dist_dir(),
        )

    def step_publish_package(self) -> dict[str, Any]:
        """Build a step that publishes the built distributions to PyPI.

        Runs `uv publish` using GitHub Actions OIDC trusted publishing.

        Returns:
            Step that publishes to PyPI using trusted publishing.
        """
        return self.step(
            self.step_publish_package,
            run=str(PackageManager.I.published_trusted_args()),
        )

    def job_build_package_permissions(self) -> dict[str, Any]:
        """Return read-only repository permissions for building the package.

        Returns:
            Permissions mapping granting `contents: read`.
        """
        return self.permission_contents()

    def steps_build_package(self) -> list[dict[str, Any]]:
        """Build the ordered steps for creating and uploading distributions.

        Returns:
            Setup, build, and artifact upload steps.
        """
        return [
            *self.steps_core_setup(),
            self.step_build_package(),
            self.step_upload_package_distributions(),
        ]

    def step_build_package(self) -> dict[str, Any]:
        """Build a step that packages the project into distributable artifacts.

        Runs `uv build` to produce wheel and source distributions in the
        `dist/` directory.

        Returns:
            Step that runs `uv build`.
        """
        return self.step(
            self.step_build_package,
            run=str(PackageManager.I.build_args()),
        )

    def step_upload_package_distributions(self) -> dict[str, Any]:
        """Build a step that uploads the distributions as a workflow artifact.

        Returns:
            Step using `actions/upload-artifact`.
        """
        return self.step_upload_artifact(
            self.step_upload_package_distributions,
            name=self.package_artifact_name(),
            path=PackageManager.I.dist_dir(),
        )

    def package_artifact_name(self) -> str:
        """Return the shared workflow-artifact name for package distributions."""
        return "package-distributions"

"""Deploy workflow extended to build the package and publish it to PyPI."""

from collections.abc import Callable
from typing import Any, override

from pyrig.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)

from pyrig_pypi.rig.tools.packages.manager import PackageManager


class DeployWorkflowConfigFile(BaseDeployWorkflowConfigFile):
    """Deploy workflow that also builds the package and publishes it to PyPI."""

    @override
    def jobs(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Return the workflow's job builders, adding the package publish builder.

        Returns:
            Tuple of base job builders plus the package build-and-publish builder.
        """
        return (
            *super().jobs(),
            self.job_package,
        )

    def job_package(self) -> dict[str, Any]:
        """Build the job that builds the package and publishes it to PyPI.

        Returns:
            Job configuration for building the package and publishing it to PyPI.
        """
        return self.job(
            self.job_package,
            permissions=self.job_package_permissions(),
            steps=self.steps_package(),
            timeout_minutes=60,
        )

    def job_package_permissions(self) -> dict[str, Any]:
        """Return the permissions for the package job.

        Requests `contents: read` to check out the repository and
        `id-token: write`, required for PyPI trusted publishing.

        Returns:
            Permissions mapping for the package job.
        """
        return {
            **self.permission_contents(),
            **self.permission_id_token(write=True),
        }

    def steps_package(self) -> list[dict[str, Any]]:
        """Build the ordered steps for the package job.

        Returns:
            Ordered list of step dicts: core setup, build the distributions,
            then publish them to PyPI.
        """
        return [
            *self.steps_core_setup(),
            self.step_build_package(),
            self.step_publish_package(),
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

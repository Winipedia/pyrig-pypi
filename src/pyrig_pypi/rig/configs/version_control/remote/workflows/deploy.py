"""Deploy workflow extended to build the package and publish it to PyPI."""

from typing import Any

from pyrig.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)

from pyrig_pypi.rig.tools.packages.manager import PackageManager


class DeployWorkflowConfigFile(BaseDeployWorkflowConfigFile):
    """Deploy workflow that also builds the package and publishes it to PyPI."""

    def jobs(self) -> dict[str, Any]:
        """Build the workflow's jobs, adding the package build-and-publish job.

        Returns:
            Dict mapping each job ID to its configuration.
        """
        return {
            **super().jobs(),
            **self.job_package(),
        }

    def job_package(self) -> dict[str, Any]:
        """Build the job that builds the package and publishes it to PyPI.

        Returns:
            Dict mapping the derived job ID to its configuration.
        """
        return self.job(
            self.job_package,
            permissions={
                **self.permission_contents(),
                **self.permission_id_token(write=True),
            },
            steps=self.steps_package(),
        )

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

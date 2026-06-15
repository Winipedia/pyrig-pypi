"""GitHub Actions workflow for deploying.

Provides the ``DeployWorkflowConfigFile`` class, which generates the
``.github/workflows/deploy.yml`` workflow file. This workflow is the final
step in the automated CI/CD pipeline and runs after a successful release.
"""

from typing import Any

from pyrig.rig.configs.base.config_file import ConfigDict
from pyrig.rig.configs.remote_version_control.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)
from pyrig.rig.tools.package_manager import PackageManager

from pyrig_pypi.rig.tools.package_index import PackageIndex


class DeployWorkflowConfigFile(BaseDeployWorkflowConfigFile):
    """Deploy workflow that adds a build-and-publish-to-PyPI job after release."""

    def jobs(self) -> ConfigDict:
        """Get the jobs for the deploy workflow.

        Combines the base jobs with the package publish job.
        """
        return {
            **super().jobs(),
            **self.job_package(),
        }

    def job_package(self) -> ConfigDict:
        """Build the job that packages and publishes the project to PyPI.

        The job runs only when the triggering workflow run succeeded. Steps
        are provided by :meth:`steps_package`.

        Returns:
            Dict mapping the derived job ID to its configuration.
        """
        return self.job(
            job_func=self.job_package,
            steps=self.steps_package(),
        )

    def steps_package(self) -> list[dict[str, Any]]:
        """Build the ordered steps for the publish-package job.

        Combines core setup with a distribution build and a PyPI publish step.
        The publish step authenticates with the ``PYPI_TOKEN`` repository secret.

        Returns:
            Ordered list of step dicts: core setup, build wheel and source
            distributions, publish to PyPI.
        """
        return [
            *self.steps_core_setup(),
            self.step_build_package(),
            self.step_publish_package(),
        ]

    def step_build_package(
        self,
        *,
        step: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a step that packages the project for distribution.

        Runs ``uv build`` to produce wheel and source distributions in the
        ``dist/`` directory.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step that runs ``uv build``.
        """
        return self.step(
            step_func=self.step_build_package,
            run=str(PackageManager.I.build_args()),
            step=step,
        )

    def step_publish_package(
        self,
        *,
        step: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a step that publishes the distributions to PyPI.

        Runs ``uv publish`` authenticated with the ``PYPI_TOKEN`` repository
        secret, injected as the ``${{ secrets.PYPI_TOKEN }}`` expression.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step that publishes to PyPI using ``PYPI_TOKEN``.
        """
        return self.step(
            step_func=self.step_publish_package,
            run=str(PackageManager.I.publish_args(token=self.insert_pypi_token())),
            step=step,
        )

    def insert_pypi_token(self) -> str:
        """Get the ``${{ secrets.PYPI_TOKEN }}`` expression.

        Returns:
            GitHub Actions expression for the ``PYPI_TOKEN`` secret.
        """
        return self.insert_var(self.pypi_token_var())

    def pypi_token_var(self) -> str:
        """Get the raw secrets expression for ``PYPI_TOKEN``.

        Returns:
            ``"secrets.PYPI_TOKEN"``
        """
        return self.secrets_var(PackageIndex.I.access_token_key())

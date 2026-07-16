"""Deploy workflow extended to build the package and publish it to PyPI."""

from typing import Any

from pyrig.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)

from pyrig_pypi.rig.tools.packages.index import PackageIndex
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

    def step_build_package(
        self,
        *,
        step: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a step that packages the project into distributable artifacts.

        Runs `uv build` to produce wheel and source distributions in the
        `dist/` directory.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step that runs `uv build`.
        """
        return self.step(
            self.step_build_package,
            run=str(PackageManager.I.build_args()),
            step=step,
        )

    def step_publish_package(
        self,
        *,
        step: dict[str, Any] | None = None,
    ) -> dict[str, Any]:
        """Build a step that publishes the built distributions to PyPI.

        Runs `uv publish` authenticated with the `PYPI_TOKEN` repository secret,
        injected as the `${{ secrets.PYPI_TOKEN }}` expression.

        Args:
            step: Additional keys to merge into the step configuration.

        Returns:
            Step that publishes to PyPI using `PYPI_TOKEN`.
        """
        return self.step(
            self.step_publish_package,
            run=str(PackageManager.I.publish_args(token=self.insert_pypi_token())),
            step=step,
        )

    def insert_pypi_token(self) -> str:
        """Return the `${{ secrets.PYPI_TOKEN }}` expression.

        Returns:
            GitHub Actions expression for the `PYPI_TOKEN` secret.
        """
        return self.insert_expression(self.pypi_token_var())

    def pypi_token_var(self) -> str:
        """Return the raw secrets expression for `PYPI_TOKEN`.

        Returns:
            The `"secrets.PYPI_TOKEN"` expression string.
        """
        return self.secrets_var(PackageIndex.I.access_token_key())

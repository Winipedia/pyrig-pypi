"""Extend deployment with the reusable package workflow."""

from collections.abc import Callable
from typing import Any, override

from pyrig.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile as BaseDeployWorkflowConfigFile,
)

from pyrig_pypi.rig.configs.version_control.remote.workflows.package import (
    PackageWorkflowConfigFile,
)


class DeployWorkflowConfigFile(BaseDeployWorkflowConfigFile):
    """Include package publishing in the deployment workflow."""

    @override
    def jobs(self) -> tuple[Callable[[], dict[str, Any]], ...]:
        """Return the base deployment jobs and the package workflow call."""
        return (*super().jobs(), self.job_package)

    def job_package(self) -> dict[str, Any]:
        """Call the reusable package build and publish workflow."""
        return self.job_workflow_call(
            self.job_package,
            workflow=PackageWorkflowConfigFile,
        )

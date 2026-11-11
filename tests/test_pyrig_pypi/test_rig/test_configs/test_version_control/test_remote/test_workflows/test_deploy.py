"""Tests for the package deployment workflow call."""

from pyrig_pypi.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile,
)


class TestDeployWorkflowConfigFile:
    """Test package workflow integration."""

    def test_job_package(self) -> None:
        """Check the package call's reference and permissions."""
        job = DeployWorkflowConfigFile.I.job_package()
        assert job["job_id"] == "package"
        assert job["uses"] == "$/.github/workflows/package.yml"
        assert job["permissions"] == {"contents": "read", "id-token": "write"}
        assert "secrets" not in job
        assert "runs-on" not in job
        assert "environment" not in job
        assert "steps" not in job

    def test_jobs(self) -> None:
        """Check the package call is included alongside base jobs."""
        workflow = DeployWorkflowConfigFile.I
        assert workflow.job_package in workflow.jobs()

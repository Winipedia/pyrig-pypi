"""Test module."""

from pyrig_pypi.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile,
)


class TestDeployWorkflowConfigFile:
    """Test class."""

    def test_job_package(self) -> None:
        """Test method."""
        job = DeployWorkflowConfigFile.I.job_package()
        assert isinstance(job, dict)
        assert job["job_id"] == "package"
        assert job["permissions"] == {
            "contents": "read",
            "id-token": "write",
        }

    def test_job_package_permissions(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.job_package_permissions() == {
            "contents": "read",
            "id-token": "write",
        }

    def test_jobs(self) -> None:
        """Test method."""
        workflow = DeployWorkflowConfigFile.I
        jobs = workflow.jobs()
        assert isinstance(jobs, tuple)
        assert workflow.job_package in jobs
        assert len(jobs) >= 1

    def test_step_build_package(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.step_build_package() == {
            "id": "build-package",
            "name": "Build Package",
            "run": "uv build",
        }

    def test_step_publish_package(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.step_publish_package() == {
            "id": "publish-package",
            "name": "Publish Package",
            "run": "uv publish --trusted-publishing=always",
        }

    def test_steps_package(self) -> None:
        """Test method."""
        steps = DeployWorkflowConfigFile.I.steps_package()
        assert isinstance(steps, list)
        names = {step["name"] for step in steps}
        assert {"Build Package", "Publish Package"}.issubset(names)

"""Test module."""

from pyrig_pypi.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile,
)


class TestDeployWorkflowConfigFile:
    """Test class."""

    def test_jobs(self) -> None:
        """Test method."""
        jobs = DeployWorkflowConfigFile.I.jobs()
        assert isinstance(jobs, dict)
        assert "package" in jobs
        assert len(jobs) >= 1

    def test_job_package(self) -> None:
        """Test method."""
        job = DeployWorkflowConfigFile.I.job_package()
        assert isinstance(job, dict)
        assert len(job) == 1
        assert job["package"]["permissions"] == {
            "contents": "read",
            "id-token": "write",
        }

    def test_steps_package(self) -> None:
        """Test method."""
        steps = DeployWorkflowConfigFile.I.steps_package()
        assert isinstance(steps, list)
        names = {step["name"] for step in steps}
        assert {"Build Package", "Publish Package"}.issubset(names)

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

"""Test module."""

from pyrig_pypi.rig.configs.version_control.remote.workflows.deploy import (
    DeployWorkflowConfigFile,
)


class TestDeployWorkflowConfigFile:
    """Test class."""

    def test_job_build_package(self) -> None:
        """Test method."""
        job = DeployWorkflowConfigFile.I.job_build_package()
        assert isinstance(job, dict)
        assert job["job_id"] == "build-package"
        assert job["permissions"] == {"contents": "read"}
        assert job["timeout-minutes"] == 60  # noqa: PLR2004

    def test_job_build_package_permissions(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.job_build_package_permissions() == {
            "contents": "read",
        }

    def test_job_publish_package(self) -> None:
        """Test method."""
        job = DeployWorkflowConfigFile.I.job_publish_package()
        assert isinstance(job, dict)
        assert job["job_id"] == "publish-package"
        assert job["needs"] == ["build-package"]
        assert job["environment"] == "package"
        assert job["permissions"] == {"id-token": "write"}
        assert job["timeout-minutes"] == 30  # noqa: PLR2004

    def test_job_publish_package_needs(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.job_publish_package_needs() == (
            DeployWorkflowConfigFile.I.job_build_package,
        )

    def test_job_publish_package_permissions(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.job_publish_package_permissions() == {
            "id-token": "write",
        }

    def test_jobs(self) -> None:
        """Test method."""
        workflow = DeployWorkflowConfigFile.I
        jobs = workflow.jobs()
        assert isinstance(jobs, tuple)
        assert workflow.job_build_package in jobs
        assert workflow.job_publish_package in jobs

    def test_package_artifact_name(self) -> None:
        """Test method."""
        assert (
            DeployWorkflowConfigFile.I.package_artifact_name()
            == "package-distributions"
        )

    def test_step_build_package(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.step_build_package() == {
            "id": "build-package",
            "name": "Build Package",
            "run": "uv build",
        }

    def test_step_download_package_distributions(self) -> None:
        """Test method."""
        step = DeployWorkflowConfigFile.I.step_download_package_distributions()
        assert step["id"] == "download-package-distributions"
        assert step["name"] == "Download Package Distributions"
        assert step["with"] == {
            "name": "package-distributions",
            "path": "dist",
        }
        assert step["uses"].startswith("actions/download-artifact@")

    def test_step_publish_package(self) -> None:
        """Test method."""
        assert DeployWorkflowConfigFile.I.step_publish_package() == {
            "id": "publish-package",
            "name": "Publish Package",
            "run": "uv publish --trusted-publishing=always",
        }

    def test_step_upload_package_distributions(self) -> None:
        """Test method."""
        step = DeployWorkflowConfigFile.I.step_upload_package_distributions()
        assert step["id"] == "upload-package-distributions"
        assert step["name"] == "Upload Package Distributions"
        assert step["with"] == {
            "name": "package-distributions",
            "path": "dist",
            "if-no-files-found": "error",
        }
        assert step["uses"].startswith("actions/upload-artifact@")

    def test_steps_build_package(self) -> None:
        """Test method."""
        steps = DeployWorkflowConfigFile.I.steps_build_package()
        assert [step["name"] for step in steps[-2:]] == [
            "Build Package",
            "Upload Package Distributions",
        ]

    def test_steps_publish_package(self) -> None:
        """Test method."""
        steps = DeployWorkflowConfigFile.I.steps_publish_package()
        assert [step["name"] for step in steps] == [
            "Setup Package Manager",
            "Download Package Distributions",
            "Publish Package",
        ]

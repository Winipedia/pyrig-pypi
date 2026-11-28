"""Tests for the reusable package workflow."""

from pyrig_pypi.rig.configs.version_control.remote.workflows.package import (
    PackageWorkflowConfigFile,
)


class TestPackageWorkflowConfigFile:
    """Test package building and publishing."""

    def test_distributions_artifact_name(self) -> None:
        """Check the shared distributions artifact name."""
        assert (
            PackageWorkflowConfigFile.I.distributions_artifact_name() == "distributions"
        )

    def test_job_build(self) -> None:
        """Check build permissions, steps, and timeout."""
        workflow = PackageWorkflowConfigFile.I
        job = workflow.job_build()
        assert "build" in workflow.job_as_dict(workflow.job_build)
        assert job["permissions"] == {"contents": "read"}
        assert job["timeout-minutes"] == 60  # noqa: PLR2004
        assert job["steps"] == workflow.steps_configs(workflow.steps_build())
        assert "needs" not in job

    def test_job_publish(self) -> None:
        """Check publish depends on the build and uses the package environment."""
        workflow = PackageWorkflowConfigFile.I
        job = workflow.job_publish()
        assert "publish" in workflow.job_as_dict(workflow.job_publish)
        assert job["needs"] == ["build"]
        assert job["environment"] == "package"
        assert job["permissions"] == {"id-token": "write"}
        assert job["timeout-minutes"] == 30  # noqa: PLR2004
        assert job["steps"] == workflow.steps_configs(workflow.steps_publish())

    def test_job_publish_needs(self) -> None:
        """Check the build is the publish prerequisite."""
        workflow = PackageWorkflowConfigFile.I
        assert workflow.job_publish_needs() == (workflow.job_build,)

    def test_jobs(self) -> None:
        """Check both package jobs are present."""
        workflow = PackageWorkflowConfigFile.I
        assert workflow.jobs() == (workflow.job_build, workflow.job_publish)

    def test_permissions_job_build(self) -> None:
        """Check the build requests read-only checkout access."""
        assert PackageWorkflowConfigFile.I.permissions_job_build() == {
            "contents": "read",
        }

    def test_permissions_job_publish(self) -> None:
        """Check publish requests the OIDC permission."""
        assert PackageWorkflowConfigFile.I.permissions_job_publish() == {
            "id-token": "write",
        }

    def test_stem(self) -> None:
        """Check the workflow filename."""
        assert PackageWorkflowConfigFile.I.stem() == "package"

    def test_step_build_package(self) -> None:
        """Check the build command."""
        workflow = PackageWorkflowConfigFile.I
        step = workflow.step_as_dict(workflow.step_build_package)
        assert step["id"] == "build-package"
        assert step["name"] == "Build Package"
        assert step["run"] == "uv build"

    def test_step_download_distributions(self) -> None:
        """Check the artifact download."""
        workflow = PackageWorkflowConfigFile.I
        step = workflow.step_as_dict(workflow.step_download_distributions)
        assert step["id"] == "download-distributions"
        assert step["name"] == "Download Distributions"
        assert step["with"] == {"name": "distributions", "path": "dist"}
        assert step["uses"].startswith("actions/download-artifact@")

    def test_step_publish_package(self) -> None:
        """Check the trusted-publishing command."""
        workflow = PackageWorkflowConfigFile.I
        step = workflow.step_as_dict(workflow.step_publish_package)
        assert step["id"] == "publish-package"
        assert step["name"] == "Publish Package"
        assert step["run"] == "uv publish --trusted-publishing=always"

    def test_step_upload_distributions(self) -> None:
        """Check the artifact upload."""
        workflow = PackageWorkflowConfigFile.I
        step = workflow.step_as_dict(workflow.step_upload_distributions)
        assert step["id"] == "upload-distributions"
        assert step["name"] == "Upload Distributions"
        assert step["with"] == {
            "name": "distributions",
            "path": "dist",
            "if-no-files-found": "error",
        }
        assert step["uses"].startswith("actions/upload-artifact@")

    def test_steps_build(self) -> None:
        """Check build and upload follow core setup."""
        workflow = PackageWorkflowConfigFile.I
        assert workflow.steps_configs(workflow.steps_build()) == workflow.steps_configs(
            (
                *workflow.steps_core_setup(),
                workflow.step_build_package,
                workflow.step_upload_distributions,
            ),
        )

    def test_steps_publish(self) -> None:
        """Check publishing setup, artifact download, and cache configuration."""
        workflow = PackageWorkflowConfigFile.I
        steps = workflow.steps_configs(workflow.steps_publish())
        assert [step["name"] for step in steps] == [
            "Setup Package Manager",
            "Download Distributions",
            "Publish Package",
        ]
        assert steps[0]["with"]["enable-cache"] == "false"
        assert steps[1:] == [
            workflow.step_as_dict(workflow.step_download_distributions),
            workflow.step_as_dict(workflow.step_publish_package),
        ]

    def test_workflow_triggers(self) -> None:
        """Check this workflow accepts reusable calls."""
        assert PackageWorkflowConfigFile.I.workflow_triggers() == {"workflow_call": {}}

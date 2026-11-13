"""Test module."""

from pyrig_pypi.rig.configs.version_control.remote.configure import (
    ConfigureRepositoryConfigFile,
)


class TestConfigureRepositoryConfigFile:
    """Test class."""

    def test_apply_topics_script(self) -> None:
        """Test method."""
        script = ConfigureRepositoryConfigFile.I.apply_topics_script()
        assert script.startswith("topics() {")
        assert "gh api" in script
        assert "repos/${GITHUB_REPOSITORY}/topics" in script
        assert "--method=PUT" in script
        assert "{names: .topics}" in script

    def test_func_apply_topics(self) -> None:
        """Test method."""
        assert ConfigureRepositoryConfigFile.I.func_apply_topics() == "topics"

    def test_scripts(self) -> None:
        """Test method."""
        scripts = ConfigureRepositoryConfigFile.I.scripts()
        assert ConfigureRepositoryConfigFile.I.apply_topics_script() in scripts

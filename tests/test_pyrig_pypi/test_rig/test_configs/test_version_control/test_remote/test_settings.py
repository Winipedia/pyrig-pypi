"""Test module."""

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile
from pyrig_pypi.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class TestRepositorySettingsConfigFile:
    """Test class."""

    def test_settings(self) -> None:
        """Test method."""
        configs = RepositorySettingsConfigFile.I.settings()
        assert "repository" in configs
        assert "rulesets" in configs
        assert configs["topics"] == RepositorySettingsConfigFile.I.topics_configs()

    def test_topics_configs(self) -> None:
        """Test method."""
        assert (
            RepositorySettingsConfigFile.I.topics_configs()
            == PyprojectConfigFile.I.keywords()
        )

    def test_topics_key(self) -> None:
        """Test method."""
        assert RepositorySettingsConfigFile.I.topics_key() == "topics"

    def test_dependencies(self) -> None:
        """Test method."""
        assert RepositorySettingsConfigFile.I.dependencies() == (PyprojectConfigFile,)

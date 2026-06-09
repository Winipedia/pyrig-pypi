"""Test module."""

from pyrig.rig.configs.pyproject import PyprojectConfigFile as BasePyprojectConfigFile

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        configs = BasePyprojectConfigFile.I.configs()
        assert configs["project"]["keywords"] == ["pyrig"]

    def test_make_keywords(self) -> None:
        """Test method."""
        assert not hasattr(
            BasePyprojectConfigFile, PyprojectConfigFile.make_keywords.__name__
        )
        assert hasattr(
            BasePyprojectConfigFile.L, PyprojectConfigFile.make_keywords.__name__
        )
        assert BasePyprojectConfigFile.I.make_keywords() == ["pyrig"]

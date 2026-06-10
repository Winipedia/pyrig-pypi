"""Test module."""

from pyrig.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        configs = PyprojectConfigFile.I.configs()
        project = configs["project"]
        assert project["classifiers"] == PyprojectConfigFile.I.make_classifiers()
        assert project["keywords"] == PyprojectConfigFile.I.make_keywords()

    def test_make_classifiers(self) -> None:
        """Test method."""
        assert PyprojectConfigFile.I.make_classifiers() == [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
            "Operating System :: OS Independent",
            "Typing :: Typed",
        ]

    def test_make_keywords(self) -> None:
        """Test method."""
        assert PyprojectConfigFile.I.make_keywords() == ["pyrig"]

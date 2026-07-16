"""Test module."""

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class TestPyprojectConfigFile:
    """Test class."""

    def test__configs(self) -> None:
        """Test method."""
        configs = PyprojectConfigFile.I.configs()
        project = configs["project"]
        assert project["classifiers"] == PyprojectConfigFile.I.classifiers_configs()
        assert project["keywords"] == PyprojectConfigFile.I.keywords_configs()

        keys = list(project.keys())
        keywords_index = keys.index("keywords")
        classifiers_index = keys.index("classifiers")
        dependencies_index = keys.index("dependencies")
        assert keywords_index == classifiers_index - 1 == dependencies_index - 2

    def test_classifiers_configs(self) -> None:
        """Test method."""
        assert PyprojectConfigFile.I.classifiers_configs() == [
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            "Programming Language :: Python :: 3.12",
            "Programming Language :: Python :: 3.13",
            "Programming Language :: Python :: 3.14",
            "Typing :: Typed",
        ]

    def test_keywords_configs(self) -> None:
        """Test method."""
        assert PyprojectConfigFile.I.keywords_configs() == ["pyrig"]

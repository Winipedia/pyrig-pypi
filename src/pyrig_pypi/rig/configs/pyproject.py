"""Configuration management for pyproject.toml.

Provides the PyprojectConfigFile class, which generates and validates the project's
pyproject.toml according to PEP 518, 621, and 660. Covers project metadata,
runtime and development dependencies, build system configuration, and tool settings.
"""

from pyrig.rig.configs.base.config_file import ConfigDict
from pyrig.rig.configs.pyproject import PyprojectConfigFile as BasePyprojectConfigFile
from pyrig.rig.tools.pyrigger import Pyrigger


class PyprojectConfigFile(BasePyprojectConfigFile):
    """You can override methods from the base class to customize behavior."""

    def _configs(self) -> ConfigDict:
        """Override the base to add this plugins additions."""
        configs = super()._configs()
        project: ConfigDict = configs["project"]
        project["classifiers"] = self.make_classifiers()
        project["keywords"] = self.make_keywords()
        return configs

    def make_classifiers(self) -> list[str]:
        """Build the PyPI trove classifiers for the project.

        Generates a ``Programming Language :: Python :: X.Y`` classifier for every
        Python minor version in the project's supported range (derived from
        ``requires-python``), plus the fixed classifiers
        ``Programming Language :: Python``, ``Programming Language :: Python :: 3``,
        ``Programming Language :: Python :: 3 :: Only``,
        ``Operating System :: OS Independent`` and ``Typing :: Typed``.

        Returns:
            List of trove classifier strings, ready for the ``project.classifiers``
            field in pyproject.toml.
        """
        return [
            "Programming Language :: Python",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3 :: Only",
            *(
                f"Programming Language :: Python :: {v.major}.{v.minor}"
                for v in self.supported_python_versions()
            ),
            "Operating System :: OS Independent",
            "Typing :: Typed",
        ]

    def make_keywords(self) -> list[str]:
        """Get the keywords applied to every package published via this plugin.

        Adds the ``pyrig`` ecosystem keyword. It is universally accurate
        because any package published through this plugin is a pyrig project,
        and it aids discoverability of the pyrig ecosystem in PyPI search.

        Returns:
            ``["pyrig"]``
        """
        return [Pyrigger.I.name()]

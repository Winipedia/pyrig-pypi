"""Configuration management for pyproject.toml.

Provides the PyprojectConfigFile class, which generates and validates the project's
pyproject.toml according to PEP 518, 621, and 660. Covers project metadata,
runtime and development dependencies, build system configuration, and tool settings.
"""

from typing import Any

from pyrig.rig.tools.pyrigger import Pyrigger
from pyrig_dev.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyproject config that adds PyPI trove classifiers and keywords."""

    def _configs(self) -> dict[str, Any]:
        """Extend the base config with PyPI classifiers and keywords.

        Adds the ``project.classifiers`` and ``project.keywords`` fields to the
        base pyproject.toml configuration.

        Returns:
            The base configuration dict with the ``project`` table augmented.
        """
        configs = super()._configs()
        project: dict[str, Any] = configs["project"]
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
        """Get the PyPI keywords for this project.

        Adds the ``pyrig`` ecosystem keyword. It is universally accurate
        because any package published through this plugin is a pyrig project,
        and it aids discoverability of the pyrig ecosystem in PyPI search.

        Returns:
            ``["pyrig"]``
        """
        return [Pyrigger.I.name()]

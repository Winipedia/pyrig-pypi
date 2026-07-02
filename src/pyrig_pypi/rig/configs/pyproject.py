"""PyPI-specific extensions to the project's `pyproject.toml` configuration."""

from typing import Any

from pyrig.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)
from pyrig.rig.tools.pyrigger import Pyrigger


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyproject config that adds PyPI trove classifiers and keywords."""

    def _configs(self) -> dict[str, Any]:
        """Add `classifiers` and `keywords` to the `project` table.

        Returns:
            The configuration dict, with the `project` table augmented.
        """
        configs = super()._configs()
        project: dict[str, Any] = configs["project"]
        project["classifiers"] = self.make_classifiers()
        project["keywords"] = self.make_keywords()
        return configs

    def make_classifiers(self) -> list[str]:
        """Build the PyPI trove classifiers for the project.

        Includes a `Programming Language :: Python :: X.Y` classifier for every
        Python minor version the project supports, alongside fixed classifiers
        declaring the project as Python 3 only, OS independent, and typed.

        Returns:
            Trove classifier strings for the `project.classifiers` field.
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
        """Build the PyPI keywords for the project.

        Returns:
            A single-element list containing the pyrig executable name, to
            aid discoverability of the pyrig ecosystem in PyPI search.
        """
        return [Pyrigger.I.name()]

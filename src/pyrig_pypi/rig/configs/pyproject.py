"""PyPI-specific extensions to the project's `pyproject.toml` configuration."""

from typing import Any

from pyrig.core.iterate import dict_insert
from pyrig.rig.configs.pyproject import (
    PyprojectConfigFile as BasePyprojectConfigFile,
)


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyproject config that adds PyPI trove classifiers and a keywords field."""

    def _configs(self) -> dict[str, Any]:
        """Add `classifiers` and `keywords` to the `project` table.

        Returns:
            The configuration dict, with the `project` table augmented.
        """
        configs = super()._configs()
        project = configs["project"]
        keys = list(project.keys())
        dependencies_index = keys.index("dependencies")

        dict_insert(
            project,
            index=dependencies_index,
            key="classifiers",
            value=sorted(self.classifiers_configs()),
        )
        dict_insert(
            project,
            index=dependencies_index,
            key="keywords",
            value=sorted(self.keywords_configs()),
        )
        return configs

    def classifiers_configs(self) -> list[str]:
        """Build the PyPI trove classifiers for the project.

        Includes a `Programming Language :: Python :: X.Y` classifier for every
        Python minor version the project supports, alongside fixed classifiers
        declaring the project as Python 3 only, OS independent, and typed.

        Returns:
            Trove classifier strings for the `project.classifiers` field.
        """
        return [
            "Operating System :: OS Independent",
            "Programming Language :: Python :: 3 :: Only",
            *(
                f"Programming Language :: Python :: {v.major}.{v.minor}"
                for v in self.supported_python_versions()
            ),
            "Typing :: Typed",
        ]

    def keywords_configs(self) -> list[str]:
        """Build the default PyPI keywords for the project.

        Returns:
            An empty list; override to scaffold default keywords.
        """
        return []

    def keywords(self) -> list[str]:
        """Retrieve the `keywords` from the `project` table.

        Returns:
            The keywords currently set in `pyproject.toml`, or an empty list if
            none are set.
        """
        return self.safe_load().get("project", {}).get("keywords", [])

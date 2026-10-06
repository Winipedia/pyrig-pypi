"""PyPI-specific extension of GitHub repository settings."""

from collections.abc import Iterable
from typing import Any

from pyrig.rig.configs.base.config_file import ConfigFile
from pyrig.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as BaseRepositorySettingsConfigFile,
)

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class RepositorySettingsConfigFile(BaseRepositorySettingsConfigFile):
    """Repository settings config that mirrors PyPI keywords as GitHub topics."""

    def dependencies(self) -> Iterable[type[ConfigFile[Any]]]:
        """Return the list of configuration file classes this config depends on.

        Adds the PyprojectConfigFile as a dependency as it needs the project's PyPI
        keywords to mirror them as GitHub topics.

        Returns:
            The base dependencies plus `PyprojectConfigFile`.
        """
        return (*super().dependencies(), PyprojectConfigFile)

    def settings(self) -> dict[str, Any]:
        """Add the `topics` key, mirroring the project's PyPI keywords.

        Returns:
            The configuration dict, with a sorted `topics` list added
            alongside the base `repository` and `rulesets` keys.
        """
        return {
            **super().settings(),
            self.topics_key(): sorted(self.topics_configs()),
        }

    def topics_configs(self) -> list[str]:
        """Return the GitHub topics for the repository.

        Returns:
            The keywords currently set in the project's `pyproject.toml`.
        """
        return PyprojectConfigFile.I.keywords()

    def topics_key(self) -> str:
        """Return `"topics"`, the top-level key for the repository's GitHub topics."""
        return "topics"

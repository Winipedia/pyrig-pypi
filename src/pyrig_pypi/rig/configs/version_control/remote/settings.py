"""PyPI-specific extension of GitHub repository settings."""

from typing import Any

from pyrig.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile as BaseRepositorySettingsConfigFile,
)

from pyrig_pypi.rig.configs.pyproject import PyprojectConfigFile


class RepositorySettingsConfigFile(BaseRepositorySettingsConfigFile):
    """Repository settings config that mirrors PyPI keywords as GitHub topics."""

    def _configs(self) -> dict[str, Any]:
        """Add the `topics` key, mirroring the project's PyPI keywords.

        Returns:
            The configuration dict, with a sorted `topics` list added
            alongside the base `repository` and `rulesets` keys.
        """
        return {
            **super()._configs(),
            self.topics_key(): sorted(self.topics_configs()),
        }

    def topics_configs(self) -> list[str]:
        """Return the GitHub topics for the repository.

        Returns:
            The project's PyPI keywords, unmodified.
        """
        return PyprojectConfigFile.I.keywords_configs()

    def topics_key(self) -> str:
        """Return `"topics"`, the top-level key for the repository's GitHub topics."""
        return "topics"

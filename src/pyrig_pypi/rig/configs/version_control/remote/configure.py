"""PyPI-specific extension of `.github/configure.sh`."""

from pyrig.rig.configs.version_control.remote.configure import (
    ConfigureRepositoryConfigFile as BaseConfigureRepositoryConfigFile,
)

from pyrig_pypi.rig.configs.version_control.remote.settings import (
    RepositorySettingsConfigFile,
)


class ConfigureRepositoryConfigFile(BaseConfigureRepositoryConfigFile):
    """Configure script extended to sync the repository's GitHub topics."""

    def scripts(self) -> tuple[str, ...]:
        """Add the `topics` function to the scripts this file defines.

        Returns:
            The base scripts, plus `apply_topics_script()`.
        """
        return (
            *super().scripts(),
            self.apply_topics_script(),
        )

    def apply_topics_script(self) -> str:
        """Return the `topics` shell function as a multi-line string.

        Returns:
            Function definition that wraps the `topics` key of the settings
            file into the body the GitHub topics endpoint expects, then
            `PUT`s it to replace the repository's topics.
        """
        settings_path = RepositorySettingsConfigFile.I.path().as_posix()
        topics_key = RepositorySettingsConfigFile.I.topics_key()
        endpoint = f"repos/${{{self.repo_variable()}}}/topics"
        extract = f"jq '{{names: .{topics_key}}}' {settings_path}"
        api_call = f'gh api "{endpoint}" --method=PUT --input=-'
        return f"""{self.apply_topics_function()}() {{
  {extract} | {api_call}
}}"""

    def apply_topics_function(self) -> str:
        """Return `"topics"`, the function name."""
        return "topics"

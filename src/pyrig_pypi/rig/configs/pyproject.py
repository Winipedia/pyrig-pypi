"""Configuration management for pyproject.toml.

Provides the PyprojectConfigFile class, which generates and validates the project's
pyproject.toml according to PEP 518, 621, and 660. Covers project metadata,
runtime and development dependencies, build system configuration, and tool settings.
"""

from pyrig.rig.configs.base.config_file import ConfigDict
from pyrig.rig.configs.pyproject import PyprojectConfigFile as BasePyprojectConfigFile
from pyrig.rig.tools.pyrigger import Pyrigger


class PyprojectConfigFile(BasePyprojectConfigFile):
    """Pyproject config that tags published packages with the pyrig keyword."""

    def _configs(self) -> ConfigDict:
        """Build the pyproject.toml structure with the pyrig keyword added.

        Extends the base configuration by adding ``project.keywords`` so that
        every package published through this plugin is discoverable as part of
        the pyrig ecosystem on PyPI. The keyword merge is additive: any
        project-specific keywords already present on disk are preserved.

        Returns:
            The base configuration dict with ``project.keywords`` set.
        """
        configs = super()._configs()
        configs["project"]["keywords"] = self.make_keywords()
        return configs

    def make_keywords(self) -> list[str]:
        """Get the keywords applied to every package published via this plugin.

        Adds the ``pyrig`` ecosystem keyword. It is universally accurate
        because any package published through this plugin is a pyrig project,
        and it aids discoverability of the pyrig ecosystem in PyPI search.

        Returns:
            ``["pyrig"]``
        """
        return [Pyrigger.I.name()]

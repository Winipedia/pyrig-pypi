"""Programming language tool wrapper.

Wraps ProgrammingLanguage commands and information.
"""

from pyrig.rig.tools.package_manager import PackageManager
from pyrig.rig.tools.programming_language import (
    ProgrammingLanguage as BaseProgrammingLanguage,
)


class ProgrammingLanguage(BaseProgrammingLanguage):
    """You can override methods from the base class to customize behavior."""

    def image_url(self) -> str:
        """Override to use pyversion badge instead of a static logo."""
        return (
            f"https://img.shields.io/pypi/pyversions/{PackageManager.I.project_name()}"
        )

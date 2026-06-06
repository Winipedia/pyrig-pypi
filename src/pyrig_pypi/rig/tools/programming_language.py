"""Programming language tool wrapper.

Wraps ProgrammingLanguage commands and information.
"""

from pyrig.rig.tools.package_manager import PackageManager
from pyrig.rig.tools.programming_language import (
    ProgrammingLanguage as BaseProgrammingLanguage,
)


class ProgrammingLanguage(BaseProgrammingLanguage):
    """Programming language tool that badges the project with PyPI pyversions."""

    def image_url(self) -> str:
        """Override to use pyversion badge instead of a static logo."""
        return (
            f"https://img.shields.io/pypi/pyversions/{PackageManager.I.project_name()}"
        )

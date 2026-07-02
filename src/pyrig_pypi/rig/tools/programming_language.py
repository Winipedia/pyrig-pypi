"""PyPI-specific override of the project's Python language badge."""

from pyrig.rig.tools.package_manager import PackageManager
from pyrig.rig.tools.programming_language import (
    ProgrammingLanguage as BaseProgrammingLanguage,
)


class ProgrammingLanguage(BaseProgrammingLanguage):
    """Programming language tool that badges the project with PyPI pyversions."""

    def image_url(self) -> str:
        """Return the badge URL for the project's supported Python versions."""
        return (
            f"https://img.shields.io/pypi/pyversions/{PackageManager.I.project_name()}"
        )

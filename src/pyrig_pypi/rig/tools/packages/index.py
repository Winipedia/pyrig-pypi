"""PyPI index integration for the project's badges and links."""

from typing import override

from pyrig.rig.tools.base.tool import Group, Tool
from pyrig.rig.tools.packages.manager import PackageManager


class PackageIndex(Tool):
    """PyPI badge and metadata for the project's package index listing.

    Badges the project with its current PyPI version and links to the project's
    PyPI page.
    """

    @override
    def dev_dependencies(self) -> tuple[str, ...]:
        """Return an empty tuple; `pypi` is not an installable dev dependency."""
        return ()

    @override
    def group(self) -> str:
        """Return `Group.PROJECT_INFO`."""
        return Group.PROJECT_INFO

    @override
    def image_url(self) -> str:
        """Return the shields.io badge URL for the project's current PyPI version."""
        repo = PackageManager.I.project_name()
        return f"https://img.shields.io/pypi/v/{repo}?logo=pypi&logoColor=white"

    @override
    def link_url(self) -> str:
        """Return the URL of the project's PyPI page."""
        repo = PackageManager.I.project_name()
        return f"https://pypi.org/project/{repo}"

    @override
    def name(self) -> str:
        """Return `"pypi"`."""
        return "pypi"

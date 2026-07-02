"""PyPI index integration for the project's badges, links, and publish token."""

from pyrig.rig.tools.base.tool import Group, Tool
from pyrig.rig.tools.package_manager import PackageManager


class PackageIndex(Tool):
    """PyPI badge and metadata for the project's package index listing.

    Badges the project with its current PyPI version linking to the project's
    PyPI page, and names the CI secret used to authenticate PyPI uploads.
    """

    def name(self) -> str:
        """Return `"pypi"`."""
        return "pypi"

    def group(self) -> str:
        """Return `Group.PROJECT_INFO`."""
        return Group.PROJECT_INFO

    def image_url(self) -> str:
        """Return the shields.io badge URL for the project's current PyPI version."""
        repo = PackageManager.I.project_name()
        return f"https://img.shields.io/pypi/v/{repo}?logo=pypi&logoColor=white"

    def link_url(self) -> str:
        """Return the URL of the project's PyPI page."""
        repo = PackageManager.I.project_name()
        return f"https://pypi.org/project/{repo}"

    def dev_dependencies(self) -> tuple[str, ...]:
        """Return an empty tuple; `pypi` is not an installable dev dependency."""
        return ()

    def access_token_key(self) -> str:
        """Return `"PYPI_TOKEN"`, the env var name for the PyPI access token."""
        return "PYPI_TOKEN"

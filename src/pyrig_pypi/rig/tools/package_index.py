"""Package index tool wrapper.

Wraps commands and information of the package index tool.
"""

from pyrig.rig.tools.base.tool import Group, Tool
from pyrig.rig.tools.package_manager import PackageManager


class PackageIndex(Tool):
    """PyPI package index wrapper.

    Constructs the PyPI project URL and shields.io version badge for the
    current project. The package name is read from ``PackageManager.I.project_name()``.
    """

    def name(self) -> str:
        """Return the tool command name.

        Returns:
            ``'pypi'``
        """
        return "pypi"

    def group(self) -> str:
        """Return the badge group this tool belongs to."""
        return Group.PROJECT_INFO

    def image_url(self) -> str:
        """Get the PyPI version badge URL."""
        repo = PackageManager.I.project_name()
        return f"https://img.shields.io/pypi/v/{repo}?logo=pypi&logoColor=white"

    def link_url(self) -> str:
        """Get the PyPI project page URL."""
        repo = PackageManager.I.project_name()
        return f"https://pypi.org/project/{repo}"

    def dev_dependencies(self) -> tuple[str, ...]:
        """Get development dependencies for this tool.

        Returns an empty tuple because PyPI itself requires no extra
        development dependency; publishing is handled by the package
        manager (e.g. uv) via ``pyproject.toml``.

        Returns:
            Empty tuple.
        """
        return ()

    def access_token_key(self) -> str:
        """Get the environment variable key for the PyPI access token.

        Used in CI/CD pipelines to authenticate when publishing packages
        to PyPI.

        Returns:
            ``'PYPI_TOKEN'``
        """
        return "PYPI_TOKEN"

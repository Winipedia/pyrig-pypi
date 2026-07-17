"""Package manager tool wrapper customized for PyPI publishing.

Extends the base package manager tool with the arguments needed to
publish a package to the PyPI index.
"""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.packages.manager import PackageManager as BasePackageManager


class PackageManager(BasePackageManager):
    """Package manager that adds PyPI publish arguments to the uv commands."""

    def publish_args(self, *args: str, token: str) -> Args:
        """Construct `Args` for publishing the package to PyPI.

        Args:
            *args: Additional arguments for the publish command.
            token: PyPI authentication token.

        Returns:
            Args for `uv publish --token=<token> <args...>`.
        """
        return self.args("publish", f"--token={token}", *args)

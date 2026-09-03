"""Package manager tool wrapper customized for PyPI publishing.

Extends the base package manager tool with the arguments needed to
publish a package to the PyPI index.
"""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.packages.manager import PackageManager as BasePackageManager


class PackageManager(BasePackageManager):
    """Package manager that adds PyPI publishing arguments to uv commands."""

    def publish_args(self, *args: str) -> Args:
        """Construct `Args` for publishing the package to PyPI.

        Args:
            *args: Additional arguments for the publish command.

        Returns:
            Args for `uv publish <args...>`.
        """
        return self.args("publish", *args)

    def published_trusted_args(self, *args: str) -> Args:
        """Construct `Args` for PyPI trusted publishing with uv.

        Args:
            *args: Additional arguments for the publish command.

        Returns:
            Args for `uv publish --trusted-publishing=always <args...>`.
        """
        return self.publish_args("--trusted-publishing=always", *args)

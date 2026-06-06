"""Package manager wrapper.

Wraps PackageManager commands and information.
"""

from pyrig.core.subprocesses import Args
from pyrig.rig.tools.package_manager import PackageManager as BasePackageManager


class PackageManager(BasePackageManager):
    """Package manager that adds PyPI publish arguments to the uv commands."""

    def publish_args(self, *args: str, token: str) -> Args:
        """Construct ``Args`` for publishing the package to PyPI.

        Args:
            *args: Additional arguments for the publish command.
            token: PyPI authentication token (keyword-only).

        Returns:
            Args for ``uv publish --token <token> <args...>``.
        """
        return self.args("publish", "--token", token, *args)

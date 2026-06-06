"""Test module."""

from pyrig.rig.tools.package_manager import PackageManager


class TestPackageManager:
    """Test class."""

    def test_publish_args(self) -> None:
        """Test method."""
        result = PackageManager.I.publish_args(token="my-token")  # noqa: S106  # nosec B106
        assert result == ("uv", "publish", "--token", "my-token")

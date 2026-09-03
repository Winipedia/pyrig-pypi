"""Test module."""

from pyrig_pypi.rig.tools.packages.manager import PackageManager


class TestPackageManager:
    """Test class."""

    def test_publish_args(self) -> None:
        """Test method."""
        result = PackageManager.I.publish_args()
        assert result == ("uv", "publish")

    def test_published_trusted_args(self) -> None:
        """Test method."""
        result = PackageManager.I.published_trusted_args()
        assert result == ("uv", "publish", "--trusted-publishing=always")

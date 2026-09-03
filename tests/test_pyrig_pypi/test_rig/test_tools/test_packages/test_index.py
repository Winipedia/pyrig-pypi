"""Test module."""

from pyrig_pypi.rig.tools.packages.index import PackageIndex


class TestPackageIndex:
    """Test class."""

    def test_name(self) -> None:
        """Test method."""
        assert PackageIndex().name() == "pypi"

    def test_group(self) -> None:
        """Test method."""
        assert PackageIndex().group() == "project-info"

    def test_image_url(self) -> None:
        """Test method."""
        assert (
            PackageIndex().image_url()
            == "https://img.shields.io/pypi/v/pyrig-pypi?logo=pypi&logoColor=white"
        )

    def test_link_url(self) -> None:
        """Test method."""
        assert PackageIndex().link_url() == "https://pypi.org/project/pyrig-pypi"
        assert PackageIndex.I.link_url() == "https://pypi.org/project/pyrig-pypi"

    def test_dev_dependencies(self) -> None:
        """Test method."""
        assert PackageIndex().dev_dependencies() == ()

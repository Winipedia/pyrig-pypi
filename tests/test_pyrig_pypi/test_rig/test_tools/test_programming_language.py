"""Test module."""

from pyrig.rig.tools.programming_language import (
    ProgrammingLanguage as BaseProgrammingLanguage,
)

from pyrig_pypi.rig.tools.programming_language import ProgrammingLanguage


class TestProgrammingLanguage:
    """Test class."""

    def test_image_url(self) -> None:
        """Test method."""
        assert (
            BaseProgrammingLanguage().image_url() != ProgrammingLanguage().image_url()
        )
        assert (
            ProgrammingLanguage.I.image_url()
            == "https://img.shields.io/pypi/pyversions/pyrig-pypi"
        )

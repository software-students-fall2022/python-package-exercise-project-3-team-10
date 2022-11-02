import pytest
from converterpackageteam10 import distance_converter

class Tests:

    def example_fixture(self):
        yield

    def test_sanity_check(self, example_fixture):
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"

import pytest
from src.converterpackageteam10 import distance_converter

class Tests:

    def test_sanity_check(self):
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    
    def test_convert_meter_to_kilometer(self):
        actual = distance_converter.convert_distance("1000", "m", "km")
        expected = "1.0"
        assert actual == expected, "Expected conversion of 1000 meter to equal 1 kilometer"
    def test_convert_meter_to_kilometer_1(self):
        actual = distance_converter.convert_distance("1000", "meter", "kilometer")
        expected = "1.0"
        assert actual == expected, "Expected conversion of 1000 meter to equal 1 kilometer"
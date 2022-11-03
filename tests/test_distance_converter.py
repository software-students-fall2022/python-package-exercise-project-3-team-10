import pytest
from src.converterpackageteam10 import distance_converter

class TestDistanceConverter:
    #This is the tolerance for the conversions. Since conversions will result in 
    #  floating points, the conversion may be slightly off than the actual.
    tol = 0.00001

    # Sanity check to make sure that tests can run
    def test_sanity_check(self):
        expected = True # the value we expect to be present
        actual = True # the value we see in reality
        assert actual == expected, "Expected True to be equal to True!"
    # Sanity check to make sure that double underscore for variable means that is is private.
    def test_sanity_units_not_exist(self):
        try:
            units = distance_converter.__units
            alias_units = distance_converter.__alias_units
            conversions = distance_converter.__conversions
            assert False, "The private variables are not supposed to be accessible"
        except AttributeError as e:
            assert True
    
    def test_convert_inches_to_other(self):
        # Note: We assume that only the conversion of inches exist.
        unit1 = 'in'
        unit2List = ["in"]
        numList = [1]
        resultList = [1]
        for num, unit2, res in zip(numList, unit2List, resultList):
            #First, test the conversion from unit1 -> u2
            expected = distance_converter.convert_distance(num, unit1, unit2)
            actual = res
            assert abs(actual-expected) <= TestDistanceConverter.tol, "The conversion of " + unit1 + " to " + unit2 + " fails"
            #Then, make sure the conversion from u2 -> unit1 also works out.
            rev_expected = distance_converter.convert_distance(res, unit2, unit1)
            rev_actual = num
            assert abs(rev_actual-rev_expected) <= TestDistanceConverter.tol, "The conversion of " + unit2 + " to " + unit1 + " fails"

    def test_convert_feet_to_other(self):
        # Note: We have the addition of feet conversions.
        unit1 = 'ft'
        unit2List = ["in", "ft"]
        numList = [1, 1]
        resultList = [12, 1]
        for num, unit2, res in zip(numList, unit2List, resultList):
            #First, test the conversion from unit1 -> u2
            expected = distance_converter.convert_distance(num, unit1, unit2)
            actual = res
            assert abs(actual-expected) <= TestDistanceConverter.tol, "The conversion of " + unit1 + " to " + unit2 + " fails"
            #Then, make sure the conversion from u2 -> unit1 also works out.
            rev_expected = distance_converter.convert_distance(res, unit2, unit1)
            rev_actual = num
            assert abs(rev_actual-rev_expected) <= TestDistanceConverter.tol, "The conversion of " + unit2 + " to " + unit1 + " fails"

    def test_convert_mile_to_other(self):
        # Note: We have the addition of mile conversions.
        unit1 = 'mi'
        unit2List = ["in", "ft", "mi"]
        numList = [1, 1]
        resultList = [63360, 5280, 1]
        for num, unit2, res in zip(numList, unit2List, resultList):
            #First, test the conversion from unit1 -> u2
            expected = distance_converter.convert_distance(num, unit1, unit2)
            actual = res
            assert abs(actual-expected) <= TestDistanceConverter.tol, "The conversion of " + unit1 + " to " + unit2 + " fails"
            #Then, make sure the conversion from u2 -> unit1 also works out.
            rev_expected = distance_converter.convert_distance(res, unit2, unit1)
            rev_actual = num
            assert abs(rev_actual-rev_expected) <= TestDistanceConverter.tol, "The conversion of " + unit2 + " to " + unit1 + " fails"

    def test_convert_milimeter_to_other(self):
        # Note: We have the addition of milimeter conversions.
        unit1 = 'mm'
        unit2List = ["in", "ft", "mi", "mm"]
        numList = [25.4, 304.8, 1609344, 1]
        resultList = [1, 1, 1, 1]
        for num, unit2, res in zip(numList, unit2List, resultList):
            #First, test the conversion from unit1 -> u2
            expected = distance_converter.convert_distance(num, unit1, unit2)
            actual = res
            assert abs(actual-expected) <= TestDistanceConverter.tol, "The conversion of " + unit1 + " to " + unit2 + " fails"
            #Then, make sure the conversion from u2 -> unit1 also works out.
            rev_expected = distance_converter.convert_distance(res, unit2, unit1)
            rev_actual = num
            assert abs(rev_actual-rev_expected) <= TestDistanceConverter.tol, "The conversion of " + unit2 + " to " + unit1 + " fails"

    def test_convert_centimeter_to_other(self):
        # Note: We have the addition of milimeter conversions.
        unit1 = 'cm'
        unit2List = ["in", "ft", "mi", "mm", "cm"]
        numList = [2.54, 30.48, 160934.4, .1, 1]
        resultList = [1, 1, 1, 1, 1]
        for num, unit2, res in zip(numList, unit2List, resultList):
            #First, test the conversion from unit1 -> u2
            expected = distance_converter.convert_distance(num, unit1, unit2)
            actual = res
            assert abs(actual-expected) <= TestDistanceConverter.tol, "The conversion of " + unit1 + " to " + unit2 + " fails"
            #Then, make sure the conversion from u2 -> unit1 also works out.
            rev_expected = distance_converter.convert_distance(res, unit2, unit1)
            rev_actual = num
            assert abs(rev_actual-rev_expected) <= TestDistanceConverter.tol, "The conversion of " + unit2 + " to " + unit1 + " fails"



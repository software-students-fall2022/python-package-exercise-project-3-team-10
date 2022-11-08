import pytest
from src.converterpackageteam10 import age_converter
import re

class Test_Age_Calc:

    def test_sanity_check(self):
        expected = True # the value we expect to be present
        actual = True # the value we see in reality        
        assert actual == expected, "Expected True to be equal to True!"

    def test_valid_out_age_calc(self):
        result = age_converter.calc_age("Dec 18 2001 10:07AM", "seconds")
        assert(result, str), f"Expected {result} to be a string!"
    
    def test_valid_out_age_calc2(self):
        units = {"actual","years", "months", "weeks", "days", "hours", "minutes", "seconds"}
        actual = False
        for unit in units:
            result = age_converter.calc_age("Dec 18 2001 10:07AM", unit)
            if(unit != "actual"):
                result_format = re.compile('^[0-9]{1}[A-Z][a-z]{2}$')
                if result_format.match(result) is not None:
                    actual = False
                else:
                    actual = True
            else:
                result_format = re.compile('^[0-9] [A-Z][a-z]{3}[a-z]$')
                if result_format.match(result) is not None:
                    actual = False
                else:
                    actual = True
 
        
        assert actual == True, f"Expected {result} to be a different format!"
    

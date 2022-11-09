import pytest
from converterpackageteam10 import age_converter
import re
import datetime

class Test_Age_Calc:

    def test_sanity_check(self):
        expected = True # the value we expect to be present
        actual = True # the value we see in reality        
        assert actual == expected, "Expected True to be equal to True!"

    def test_valid_out_age_calc(self):
        result = age_converter.calc_age("Dec 18 2001 10:07AM", "seconds")
        assert isinstance(result, str), f"Expected {result} to be a string!"
    
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
    
    def test_age_calc_valid_years(self):
        result = age_converter.calc_age("Jan 1 2001 12:00AM", "years")
        today = datetime.date.today()
        expected = today.year - 2001
        assert isinstance(result, str), f"Expected {result} to be a string!"
    
    def test_age_calc_valid_months(self):
        result = age_converter.calc_age("Jan 1 2001 12:00AM", "years")
        today = datetime.date.today()
        expected = today.year - 2001
        assert expected == int(result.split()[0]), f"Expected {result} to be a string!"
    
    def test_age_calc_no_exceptions(self):
        years = [2001, 2010, 2021]
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul',
                'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        days = [1, 10, 12, 15, 18, 21, 24, 27]
        units = ['actual', 'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']
        try:
            for year in years:
                for month in months:
                    for day in days:
                        for unit in units:
                            dob = " ".join([str(month), str(day), str(year), "12:00AM"])
                            age_converter.calc_age(dob, unit)
        except ValueError as e:
            assert False, "ValueError: " + e.args[0]
        except Exception as e:
            assert False, "Exception: " + e.args[0]
        assert True
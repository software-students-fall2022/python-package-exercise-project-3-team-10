import pytest
from converterpackageteam10 import time_zone_converter
import pytz
from datetime import datetime


class Test:
    def test_exception_raised(self):
        #check if KeyError exception was raised
        with pytest.raises(KeyError) as excinfo:
            time_zone_converter.convert_timezone("XX")
        msg = excinfo.value.args[0]
        assert msg == "Expected valid ISO Alpha 2 code but got XX", "Expected valid ISO Alpha 2"

    def test_no_empty(self):
        #check for all valid isos, if the function returns a dictionary of at least length 1
        isos = ["AF", "AX", "AL", "DZ", "AS", "AD", "AO", "AI", "AQ", "AG", "AR",
                "AM", "AW", "AU", "AT", "AZ", "BS", "BH", "BD", "BB", "BY", "BE",
                "BZ", "BJ", "BM", "BT", "BO", "BQ", "BA", "BW", "BR", "IO",
                "BN", "BG", "BF", "BI", "CV", "KH", "CM", "CA", "KY", "CF", "TD",
                "CL", "CN", "CX", "CC", "CO", "KM", "CG", "CD", "CK", "CR", "CI",
                "HR", "CU", "CW", "CY", "CZ", "DK", "DJ", "DM", "DO", "EC", "EG",
                "SV", "GQ", "ER", "EE", "ET", "FK", "FO", "FJ", "FI", "FR", "GF",
                "PF", "TF", "GA", "GM", "GE", "DE", "GH", "GI", "GR", "GL", "GD",
                "GP", "GU", "GT", "GG", "GN", "GW", "GY", "HT", "VA", "HN","HK", 
                "HU", "IS", "IN", "ID", "IR", "IQ", "IE", "IM", "IL", "IT","JM", 
                "JP", "JE", "JO", "KZ", "KE", "KI", "KP", "KR", "KW", "KG",
                "LA", "LV", "LB", "LS", "LR", "LY", "LI", "LT", "LU", "MO", "MK",
                "MG", "MW", "MY", "MV", "ML", "MT", "MH", "MQ", "MR", "MU", "YT",
                "MX", "FM", "MD", "MC", "MN", "ME", "MS", "MA", "MZ", "MM", "NA",
                "NR", "NP", "NL", "NC", "NZ", "NI", "NE", "NG", "NU", "NF", "MP",
                "NO", "OM", "PK", "PW", "PS", "PA", "PG", "PY", "PE", "PH", "PN",
                "PL", "PT", "PR", "QA", "RE", "RO", "RU", "RW", "BL", "SH", "KN",
                "LC", "MF", "PM", "VC", "WS", "SM", "ST", "SA", "SN", "RS", "SC",
                "SL", "SG", "SX", "SK", "SI", "SB", "SO", "ZA", "GS", "SS", "ES",
                "LK", "SD", "SR", "SJ", "SZ", "SE", "CH", "SY", "TW", "TJ", "TZ",
                "TH", "TL", "TG", "TK", "TO", "TT", "TN", "TR", "TM", "TC", "TV",
                "UG", "UA", "AE", "GB", "US", "UM", "UY", "UZ", "VU", "VE", "VN",
                "VG", "VI", "WF", "EH", "YE", "ZM", "ZW"]
        for iso in isos:
            assert len(time_zone_converter.convert_timezone(iso)) >= 1,"Expected function to return dictionary of length 1 or more"

    def test_valid_output(self):
        #check if all timezones in output are in the the list for all timezones of a given ISO code
        expected = pytz.country_timezones["US"]
        timezones = time_zone_converter.convert_timezone("US").values()
        for timezone in timezones:
            assert(timezone in expected),"Expected output timezones to be in list of all timezones for ISO Code"
    
    def test_output_type(self):
        #check if returned value is of type dict
        actual = time_zone_converter.convert_timezone("PR")
        assert isinstance(actual,dict),"Expected output to be of type dictionary"
    
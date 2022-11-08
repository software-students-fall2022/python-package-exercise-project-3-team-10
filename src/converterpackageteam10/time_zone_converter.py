# -*- coding: utf-8 -*-
from datetime import datetime
import pytz #need pip install

def convert_timezone(code): #input is country’s ISO Alpha 2 code
    '''Converts the current time into a dictionary'''
    ''' given the country's ISO Alpha 2 code, returns a dictionary ... '''

    if code not in pytz.country_timezones:
        raise KeyError('Expected valid ISO Alpha 2 code but got ' +  code)
    timezones = pytz.country_timezones[code]
    fmt = '%I:%M%p'
    utc = datetime.now(pytz.timezone("UTC"))
    res = {}
    for timezone in timezones:
        converted = utc.astimezone(pytz.timezone(timezone)).strftime(fmt)
        if converted not in res:
            res[timezone] = converted
    return res





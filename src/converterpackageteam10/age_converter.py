import datetime
from datetime import datetime
import math


def calc_age(dob, unit):
    units = {"years", "months", "weeks", "days", "hours", "minutes", "seconds", "help"}

    my_dob = datetime.strptime(str(dob), "%b %d %Y %I:%M%p")

    # if unit in units:
    today = datetime.now()
    timedelta = today - my_dob
    days = timedelta.days
    weeks = timedelta.days // 7
    hours = timedelta.seconds // 3600 + days * 24
    minutes = timedelta.seconds // 60 + hours * 60
    seconds = timedelta.seconds + minutes * 60

    if(my_dob.month>today.month):
        curr_years = today.year-my_dob.year-1
        curr_months = abs(my_dob.month -( 12 - today.month))
        if(my_dob.day>today.day):
            curr_days = 30 - my_dob.day + today.day
        else:
            curr_days = today.day - my_dob.day
    else:
        curr_years = today.year-my_dob.year
        curr_months = today.month-my_dob.month
        curr_days = today.day-my_dob.day
    my_full_dob = datetime(curr_years, curr_months, curr_days)

    # if unit == "all":   
    #     return "You are " + str(my_full_dob.year) + "\x1B[3m years\x1B[0m, " + " " + str(my_full_dob.month) + "\x1B[3m months\x1B[0m and " + " " + str(my_full_dob.day) + "\x1B[3m days\x1B[0m old" + "\nIn another world you are \n" + str(weeks) + " \x1B[3m weeks\x1B[0m old " + " \n" + str(days) + " \x1B[3m days\x1B[0m old " + " \n" +str(hours)+ " \x1B[3m hours\x1B[0m old or" + " \n" + str(minutes) + " \x1B[3m minutes\x1B[0m old or" + " \n" + str(seconds) + " \x1B[3m seconds\x1B[0m old" 

    if unit == "help":
        return "You can use the following units: \n" + "years, months, weeks, days, hours, minutes, seconds" + "\n" + "Example: calc_age('Jan 1 2000 1:33PM', 'years')"
    elif unit == "years":
        return str(my_full_dob.years) + " \x1B[3m years\x1B[0m  old "
    elif unit == "months":
        return str(my_full_dob.months) + " \x1B[3m months\x1B[0m  old "
    elif unit == "weeks":
        return str(weeks) + " \x1B[3m weeks\x1B[0m old "
    elif unit == "days":
        return str(days) + " \x1B[3m days\x1B[0m old "
    elif unit == "hours":
        return str(hours) + " \x1B[3m minutes\x1B[0m old "
    elif unit == "minutes":
        return str(minutes) + " minutes"
    elif unit == "seconds":
        return str(seconds) + " \x1B[3m secpmds\x1B[0m old "
    else:
        return "Invalid input"


# def get_age_in_diff_calender(dob, cal):
#     calanders = {"gregorian", "julian", "hebrew", "islamic", "chinese", "mayan", "coptic", "ethiopian", "ethiopic", "indian", "persian", "republican", "roc"}

#     return str(dob)
print(calc_age("Dec 18 2001 10:07AM", "years"))

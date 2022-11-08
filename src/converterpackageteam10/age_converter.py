import datetime
from datetime import datetime

def calc_age(dob, unit):
    """ Given a date of birth, returns a conversion based on the unit desired. """

    try:
        my_dob = datetime.strptime(str(dob), "%b %d %Y %I:%M%p")
    except ValueError:
        return "Invalid date format"

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

    months = curr_years * 12 + curr_months


    if unit == "actual":
        return str(my_full_dob.year) + "\x1B[3m years\x1B[0m, " + " " + str(my_full_dob.month) + "\x1B[3m months\x1B[0m and " + " " + str(my_full_dob.day) + "\x1B[3m days\x1B[0m old"
    elif unit == "years":
        return str(my_full_dob.year) + " \x1B[3m years\x1B[0m  old "
    elif unit == "months":
        return str(months) + " \x1B[3m months\x1B[0m  old "
    elif unit == "weeks":
        return str(weeks) + " \x1B[3m weeks\x1B[0m old "
    elif unit == "days":
        return str(days) + " \x1B[3m days\x1B[0m old "
    elif unit == "hours":
        return str(hours) + " \x1B[3m hours\x1B[0m old "
    elif unit == "minutes":
        return str(minutes) + " \x1B[3m minutes\x1B[0m old "
    elif unit == "seconds":
        return str(seconds) + " \x1B[3m seconds\x1B[0m old "
    else:
        return "Invalid input"

def help():
    """Provides some help with using the calc_age function to the user"""

    return "Age_converter.calc_age: \n\tYou can use the following units: \n\t" + "help, actuall, years, months, weeks, days, hours, minutes, seconds" + "\n\t" + "Example: calc_age('Jan 1 2000 1:33PM', 'years')"


# def get_age_in_diff_calender(dob, cal):
#     calanders = {"gregorian", "julian", "hebrew", "islamic", "chinese", "mayan", "coptic", "ethiopian", "ethiopic", "indian", "persian", "republican", "roc"}

#     return str(dob)

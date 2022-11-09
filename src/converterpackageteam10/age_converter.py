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

    if (my_dob.month>today.month):
        curr_years = today.year-my_dob.year-1
        curr_months = abs(my_dob.month -( 12 - today.month))
    else:
        curr_years = today.year-my_dob.year
        curr_months = today.month-my_dob.month
    if (my_dob.day>today.day):
        curr_days = 30 - my_dob.day + today.day
    else:
        curr_days = today.day - my_dob.day
    
    print("\t\tcurr days:   "+str(curr_days)+ "\n")
    
    my_full_dob = datetime(curr_years, curr_months, curr_days)

    months = curr_years * 12 + curr_months


    if unit == "actual":
        return str(my_full_dob.year) + " years " + str(my_full_dob.month) + " months and " + str(my_full_dob.day) + " days old"
    elif unit == "years":
        return str(my_full_dob.year) + " years old"
    elif unit == "months":
        return str(months) + " months old"
    elif unit == "weeks":
        return str(weeks) + " weeks old"
    elif unit == "days":
        return str(days) + " days old"
    elif unit == "hours":
        return str(hours) + " hours old"
    elif unit == "minutes":
        return str(minutes) + " minutes old"
    elif unit == "seconds":
        return str(seconds) + " seconds old"
    else:
        return "Invalid input"

def help():
    """Provides some help with using the calc_age function"""
    print("\tcalc_age(dob, unit):")
    print("\t\tInput dob in the following format: MTH DAY YEAR TIME")
    print("\t\tThese are the available units to convert into:", __units())
    print("\t\tExample:")
    print("\t\t\t>> calc_age('Jan 1 2000 1:33PM', 'years')")
    print("\t\t\t" + calc_age('Jan 1 2000 1:33PM', 'years'))

def __units():
    return ['actual', 'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']

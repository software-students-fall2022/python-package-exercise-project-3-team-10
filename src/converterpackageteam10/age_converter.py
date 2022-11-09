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

    if (my_dob.month > today.month):
        curr_years = today.year-my_dob.year-1
        curr_months = abs(my_dob.month - (12 - today.month))
    else:
        curr_years = today.year-my_dob.year
        curr_months = today.month-my_dob.month
    if (my_dob.day > today.day):
        curr_days = my_dob.day - today.day# +30
        curr_months = curr_months - 1
    else:
        curr_days = today.day - my_dob.day
    # zero out the time portion of the datetime object
    if(curr_months<1):
        temp_months = 1
        curr_months = 1
    else:
        temp_months = 0
    # 
    if(curr_years<1):
        temp_years = 1
        curr_years = 1
    else:
        temp_years = 0
    # 
    if(curr_days<1):
        temp_days = 1
        curr_days = 1
    else:
        temp_days = 0
        
    my_full_dob = datetime(curr_years, curr_months, curr_days)

    months = curr_years * 12 + curr_months

    if unit == "actual":
        return str(my_full_dob.year - temp_years) + " years " + str(my_full_dob.month - temp_months) + " months and " + str(my_full_dob.day - temp_days) + " days old"
    elif unit == "years":
        return str(my_full_dob.year - temp_years) + " years old"
    elif unit == "months":
        return str(months - temp_months) + " months old"
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


# def main():
#     years = [2001, 2010, 2021]
#     months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
#     days = [1, 7, 10, 12, 15, 18, 21, 24, 27]
#     times = ["12:00AM", "5:43PM", "11:30AM", "2:00PM", "7:20PM"]
#     units = ['actual']#, 'years', 'months', 'weeks', 'days', 'hours', 'minutes', 'seconds']
#     try:
#         for year in years:
#             for month in months:
#                 for day in days:
#                     for time in times:
#                         for unit in units:
#                             dob = " ".join([str(month), str(day), str(year), time])
#                             age = calc_age(dob, unit)
#     except ValueError as e:
#         print("Error1: " + str(dob) + " " + unit + " " + str(e) + " " + str(age))
#     except Exception as e:
#         print("Error2: " + str(dob) + " " + unit + " " + str(e) + " " + str(age))
#     # print(calc_age('Oct 21 2001 12:00AM', 'actual'))   
    
# main()
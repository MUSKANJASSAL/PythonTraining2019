# import datetime

import datetime as dt

today = dt.datetime.today()
#now = dt.datetime.now()
print("Its:",today)
print(today.year)     # Return the year
print(today.strftime("%A"))     # Return name of weekday, full version
print(today.strftime("%a"))  # Weekday, short version
print(today.strftime("%B"))    # Display the name of the month
print(today.strftime("%b"))   # Month name short version
print(today.strftime("%w"))    # Weekday as a number 0-6, 0 is Sunday
print(today.strftime("%d"))  # Day of month 01-31
print(today.strftime("%m"))   # Month as a number 01-12
print(today.strftime("%y"))    # Year, short version, without century
print(today.strftime("%Y"))   # Year, full version
print(today.strftime("%H"))  # Hour 00-23
print(today.strftime("%I"))  # Hour 00-12
print(today.strftime("%M"))    # Minute 00-59
print(today.strftime("%S"))     # Second 00-59
print(today.strftime("%p"))     # AM/PM
print(today.strftime("%z"))    # UTC offset
print(today.strftime("%Z"))   # Timezone
print(today.strftime("%x"))    # Local version of date
print(today.strftime("%X"))    # Local version of time
print(today.strftime("%j"))   # Day number of year 001-366

tomorrow = dt.datetime(2019, 6, 25, 12, 45, 33, 12)
print("Tomorrow is:",tomorrow)

howManyDays = tomorrow - today
print("How Many Days: ",howManyDays)
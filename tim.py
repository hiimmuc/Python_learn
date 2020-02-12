import time
import datetime
import calendar
import pytz

# datetime.date(Y, M, D)
# datetime.time(h, m, s, ms)
# datetime.datetime(Y, M, D, h, m, s, ms)

# print("\t" * 9 + "Calendar of: ")
# calendar.prcal(2020, w=3)

# day_of_the_week = calendar.weekday(2000, 11, 18)
# print(day_of_the_week)
# print(calendar.leapdays(0, 2020))

print(f"WEEKDAYS:\n {calendar.weekheader(3)}")
print(f"Current time:\n {time.asctime(time.localtime(time.time()))}")

# today = datetime.date.today()
# print(datetime.datetime.now(tz=pytz.UTC) + datetime.timedelta(hours=24))
# print(datetime.time(7, 2, 20))
datetime_pacific = datetime.datetime.now(
    tz=pytz.UTC).astimezone(pytz.timezone('America/Chicago'))
# print(datetime_pacific)
# for tz in pytz.all_timezones:
#     print(tz)

# string formating with date:
# 2020-02-11 -> February 2,2020
# strftime() f->formating
print(datetime_pacific.strftime('%B %d, %Y'))
# strptime() p->parsing
print(datetime.datetime.strptime('February 11, 2020', '%B %d, %Y'))
# https: // github.com/timofurrer/maya
# can use link above to handle datetime problems

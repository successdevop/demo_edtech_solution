import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')

start = datetime.date(2026, 4, 1)
print(start)

pretty_start = start.strftime("%A %b %B %Y")
print(pretty_start)

year = start.year
month = start.month
day = start.day

print("year: {}, month: {}, day: {}".format(year, month, day))

today = datetime.date.today()
print(today)
print(today.strftime('%b'))
print(today.weekday())


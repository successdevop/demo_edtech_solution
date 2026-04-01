import datetime
import locale

locale.setlocale(locale.LC_ALL, "")

start = datetime.date(2026, 4, 1)
print(start)
readable = start.strftime('%A %d %B %Y')
print(readable)

duration = datetime.timedelta(days=15, hours=2)
print(duration)
end = start + duration
print(end)
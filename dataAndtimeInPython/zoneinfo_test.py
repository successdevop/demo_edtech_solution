from datetime import datetime, timezone
try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo


utc_now = datetime.now(timezone.utc)
# print(utc_now)

local_now = utc_now.astimezone()
print(local_now)

new_york_tz = zoneinfo.ZoneInfo('America/New_York')
ny_now = utc_now.astimezone(tz=new_york_tz)
# print(ny_now)
# print()

france_tz = zoneinfo.ZoneInfo("Africa/lagos")
france_now = utc_now.astimezone(france_tz)
# print(france_now)

# print(zoneinfo.available_timezones())
# for keyzone in zoneinfo.available_timezones():
#     if "Paris" in keyzone:
#         print(keyzone)
#     if "London" in keyzone:
#         print(keyzone)
#     if "Hong" in keyzone:
#         print(keyzone)
#     if "Nairobi" in keyzone:
#         print(keyzone)

utc_now = datetime.now(timezone.utc)

paris_tz = zoneinfo.ZoneInfo("Europe/Paris")
paris_now = str(utc_now.astimezone(paris_tz)).split(".")[0]
print(f"Paris time is : {paris_now}")

london_tz = zoneinfo.ZoneInfo("Europe/London")
london_now = str(utc_now.astimezone(london_tz)).split(".")[0]
print(f"London time is : {london_now}")

hongKong_tz = zoneinfo.ZoneInfo("Asia/Hong_Kong")
hongKong_now = str(utc_now.astimezone(hongKong_tz)).split(".")[0]
print(f"Hong Kong time is : {hongKong_now}")

nairobi_tz = zoneinfo.ZoneInfo("Africa/Nairobi")
nairobi_now = str(utc_now.astimezone(nairobi_tz)).split(".")[0]
print(f"Nairobi time is : {nairobi_now}")




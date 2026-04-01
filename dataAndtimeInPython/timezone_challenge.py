from datetime import datetime, timezone

try:
    import zoneinfo
except ImportError:
    from backports import zoneinfo


zones = ("Europe/Paris", "Europe/London", "Asia/Hong_Kong", "Africa/Nairobi")

utc_now = datetime.now(timezone.utc)

for each_country_timezone in zones:
    country_tz = zoneinfo.ZoneInfo(each_country_timezone)
    country_tz_now = utc_now.astimezone(country_tz)
    print(f"{str(country_tz).split('/')[1]} timezone is: {str(country_tz_now).split('.')[0]}")
import json
import urllib.request

temp_data_source = ("https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json")


with urllib.request.urlopen(temp_data_source) as temp_data:
    data = temp_data.read().decode('utf-8')
    anomalies = json.loads(data)


print(anomalies)
# print(anomalies['description'])
print("+=*"*40)
for year, val in anomalies['data'].items():
    year, val = year, float(val)
    print(f"{year} ... {val:6.2f}")
print("+=*"*40)
# print(anomalies['citation'])

# print(anomalies)


# temp = "temp_global.json"
#
# with open(temp, 'r', encoding='utf-8') as temperature:
#     data = json.load(temperature)
#
#

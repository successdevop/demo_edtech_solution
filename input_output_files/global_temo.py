import json

temp = "temp_global.json"

with open(temp, 'r', encoding='utf-8') as temperature:
    data = json.load(temperature)
print(data)

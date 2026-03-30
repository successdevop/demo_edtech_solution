import csv

csv_filename = "country_info.txt"

dialect = csv.excel
dialect.delimiter = '|'

countries_list = {}

with open(csv_filename, encoding='utf-8', newline='') as countries:
    reader = countries.readline().strip('\n').split(dialect.delimiter)
    for index, heading in enumerate(reader):
        reader[index] = heading.casefold()

    country_data = csv.DictReader(countries, dialect=dialect, fieldnames=reader)
    for country in country_data:
        countries_list[country['country']] = country


while True:
    country_key = input("Please enter the name of a country: ")
    if country_key in countries_list:
        chosen_country = countries_list[country_key]
        print(f"The capital of {country_key} is => {chosen_country['capital']}")
    elif country_key == "quit":
        break

print(countries_list)
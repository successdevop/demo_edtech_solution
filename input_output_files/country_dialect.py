import csv

csv_filename = "country_info.txt"

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    sample = ""
    for i in range(3):
        sample += csv_file.readline()

    data = csv.Sniffer().sniff(sample)
    csv_file.seek(0)
    reader = csv.reader(csv_file, dialect=data)
    for row in reader:
        print(row)

print("*"*80)

attributes = [
    "delimiter",
    "doublequote",
    "escapechar",
    "lineterminator",
    "quotechar",
    "quoting",
    "skipinitialspace"
]

for attribute in attributes:
    print(f"{attribute}: {getattr(data, attribute)}")

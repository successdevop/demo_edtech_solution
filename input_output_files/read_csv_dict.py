import csv

filename = 'cereal_grains.csv'

with open(filename, encoding='utf-8', newline='') as csv_filename:
    reader = csv.DictReader(csv_filename, quoting=csv.QUOTE_NONNUMERIC)
    for read in reader:
        print(read)
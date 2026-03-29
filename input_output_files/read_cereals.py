import csv

csv_filename = "cereal_grains.csv"

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    firstLine = csv_file.readline().rstrip().split(",")
    print(f"Headers: {firstLine}")
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
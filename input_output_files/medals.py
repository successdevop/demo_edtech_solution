import csv

csv_filename = "OlympicMedals_2020.csv"

with open(csv_filename, newline='', encoding='utf-8') as csv_file:
    firstLine = csv_file.readline().rstrip().split(",")
    print(firstLine)
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

import csv

csv_filename = "country_info.txt"

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    sample = csv_file.read()
    data = csv.Sniffer().sniff(sample)
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)

import csv

csv_filename = "cereal_grains.csv"
cereals = {}
with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    csv_file.readline()
    reader = csv.reader(csv_file)
    for row in reader:
        cereal, calories, fat, protein, fibre, vitamin_E = row
        cereal_dict = {
            "name": cereal,
            "calories": calories,
            "fat": fat,
            "protein": protein,
            "fibre": fibre,
            "vitamin_E": vitamin_E
        }
        cereals[cereal] = cereal_dict

print(cereal)

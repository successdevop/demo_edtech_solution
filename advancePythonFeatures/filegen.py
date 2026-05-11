import os

root = "/Users/raphtech/demo_edtech_solution/"

for root, directory, files in os.walk(root):
    print(root)
    print(directory)
    for file in files:
        if file.endswith(".py"):
            print(file)
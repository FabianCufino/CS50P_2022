import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("Could not read invalid_file.csv")

dict_1 = {}

with open(sys.argv[2], 'w', newline='') as file2:
    fieldnames = ['first', 'last', 'house']
    csv_writer = csv.DictWriter(file2, fieldnames=fieldnames)
    csv_writer.writeheader()  # Writes the header row

with open(sys.argv[1]) as file:
    csv_reader = csv.DictReader(file)

    for row in csv_reader:

        name = row['name']
        last, first = name.replace(" ","").split(",")
        house = row['house']
        #print ("first:",first,"last:", last, "house:", house )
        #dict_1.update({"first":first, "last":last, "house":house})
        lista = [first,last,house]
        #print(lista)
        with open(sys.argv[2],'a') as file2:
            writer = csv.DictWriter(file2, fieldnames=['first', 'last', 'house'])
            writer.writerow({"first": first, "last": last, "house": house})

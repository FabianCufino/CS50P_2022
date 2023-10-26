import sys
import csv
from tabulate import tabulate

if len(sys.argv) < 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")
elif sys.argv[1][-4:] != ".csv":
    sys.exit("Not a CSV file")

try:
    with open(sys.argv[1], "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    sys.exit("File does not exist")

pizzas_list = []

with open(sys.argv[1]) as file:
    reader = csv.reader(file)
    for row in reader:
        #print(row)
        list = []


        pizzas_list.append({"RegularPizza": row[0], "Small": row[1], "Large": row[2]})
    print(tabulate(pizzas_list,headers="firstrow",tablefmt="grid" ))
        #print(pizzas_list)
        #print(tabulate(pizzas_list[row]))

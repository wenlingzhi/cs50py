import sys
from tabulate import tabulate
import csv

if len(sys.argv) == 1:
    exit("Too few command-line arguments")
if ".csv" not in sys.argv[1]:
    exit("Not a csv file")
elif len(sys.argv) > 2:
    exit("Too much command-line arguments")
else:
    try:
        with open(sys.argv[1]) as file:
            table = []
            reader = csv.reader(file)
            headers = next(reader)

            for row in reader:
                table.append(row)

            print(tabulate(table,headers,tablefmt="grid"))

    except FileNotFoundError:
        exit("File does not exist")

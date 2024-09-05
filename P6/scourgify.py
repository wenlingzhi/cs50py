import sys
import csv

infile = sys.argv[1]
outfile = sys.argv[2]

if len(sys.argv)<2:
    exit("Too few command-line arguments")
if ".csv" not in sys.argv[1] and ".csv" not in sys.argv[2]:
    exit("Not a csv file")
elif len(sys.argv)> 3:
    exit("Too much command-line arguments")
else:
    try:
        with open(infile) as file:
            reader = csv.reader(file)
            rows = []
            next(reader)

            for name,house in reader:
                last,first = name.split(", ")
                rows.append({"first": first, "last": last, "house": house})

        with open(outfile,"w") as file:
            field = ["first","last","house"]
            writer = csv.DictWriter(file,fieldnames=field)
            writer.writeheader()
            writer.writerows(rows)

    except FileNotFoundError:
        exit("File does not exist")



import csv

with open('MAN01405.csv') as csvfile:
    thereader = csv.reader(csvfile)

    for row in thereader:
        print(row)


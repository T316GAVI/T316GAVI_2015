import csv

with open('MAN01405.csv') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';')

    for row in thereader:
        print(len(row))
        print(row)


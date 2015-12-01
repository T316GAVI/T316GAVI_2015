import csv

brottfluttir = []

with open('MAN01405.csv') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';')

    for row in thereader:
        brottfluttir.append(row[5])

print('Total brottfluttir: ', sum(brottfluttir))
print()

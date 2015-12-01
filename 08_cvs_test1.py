import csv

brottfluttir = []

with open('MAN01405.csv') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';')

    readingheaderrow = True
    for row in thereader:
        if readingheaderrow:
            readingheaderrow = False
        else:
            brottfluttir.append(int(row[5]))

print('Total brottfluttir: ', sum(brottfluttir))
print()

import csv

brottfluttir = []

with open('MAN01405.csv') as csvfile:
    thereader = csv.reader(csvfile, delimiter=';')

    readingheaderrow = True
    for row in thereader:
        if readingheaderrow:
            readingheaderrow = False
        else:
            try:
                brottfluttir.append(int(row[5]))
            except:
                pass

print('Total brottfluttir: ', sum(brottfluttir))
print()

import csv

with open('MAN01405.csv','r') as csvfile:
    currentdialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)

    dictreader = csv.DictReader(csvfile, dialect = currentdialect)

    firstrow = True
    for row in dictreader:
        if firstrow:
            print(row)
            firstrow = False

        if row['Íslenskir ríkisborgarar Brottfluttir'].isdigit() \
        and int(row['Íslenskir ríkisborgarar Brottfluttir']) > 3000:
            print(row['Ár'], row['Íslenskir ríkisborgarar Brottfluttir'], sep=': ')



import csv

#Stillingar
islbrott = 'Íslenskir ríkisborgarar Brottfluttir'
yearfield = 'Ár'


with open('MAN01405.csv','r') as csvfile:
    currentdialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)

    dictreader = csv.DictReader(csvfile, dialect = currentdialect)

    firstrow = True
    for row in dictreader:
        if firstrow:
            print(row)
            firstrow = False

        if row[islbrott].isdigit() \
        and int(row[islbrott]) > 3000:
            print(row[yearfield], row[islbrott], sep=': ')



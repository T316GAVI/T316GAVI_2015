import csv

with open('MAN01405.csv','r') as csvfile:
    currentdialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)

    dictreader = csv.DictReader(csvfile, dialect = currentdialect)



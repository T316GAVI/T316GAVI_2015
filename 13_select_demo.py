import psycopg2
import getpass
import random as r
import pprint

host = 'localhost'
dbname = 'gavi'

username = 'postgres' # input('User name for {}.{}: '.format(host,dbname))
pw = 'postgres' # getpass.getpass()

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")

nafn = input('Superhero: ')
verd = float(input('Beer price: '))

s = """
select d.name, l.beer, s.price
from drinkers d, likes l, frequents f, sells s
where d.name = l.drinker and d.name = f.drinker
and f.bar = s.bar and s.beer = l.beer
and d.name = %s
and s.price < %s"""

v = (nafn, verd)

cursor.execute(s,v)

records = cursor.fetchall()
pprint.pprint(records)

if len(records) > 0:
    row = records[0]

    print(row[1])


cursor.close()
conn.close()

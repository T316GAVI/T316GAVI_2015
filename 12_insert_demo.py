import psycopg2
import getpass
import random as r

host = 'localhost'
dbname = input('Database name: ') # 'gavi'

username = input('User name for {}.{}: '.format(host,dbname))  # 'postgres'
pw = getpass.getpass()  # 'postgres'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")

thesqlcommands = open('beer_demo.sql','r')
for line in thesqlcommands:
    print(line)
    cursor.execute(line.strip())

thesqlcommands.close()

conn.commit()

cursor.close()
conn.close()



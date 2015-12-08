import psycopg2
import getpass

host = 'localhost'
dbname = input('Database name: ')

username = input('User name for {}.{}: '.format(host,dbname))
pw = getpass.getpass()

conn_string = "host='{}' port='2270' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print("Connected!\n")


# Do something here...

cursor.close()
conn.close()


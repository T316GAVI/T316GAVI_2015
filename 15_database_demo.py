import psycopg2

host = 'localhost'
dbname = 'tempbase' #input('Database name: ') # 'gavi'

username = 'postgres' # input('User name for {}.{}: '.format(host,dbname))  # 'postgres'
pw = 'postgres' # getpass.getpass()  # 'postgres'

conn_string = "host='{}' dbname='{}' user='{}' password='{}'".format(host, dbname, username, pw)

print("Connecting to database {}.{} as {}".format(host, dbname, username))

conn = psycopg2.connect(conn_string)

cursor = conn.cursor()

print('Whee!')

cursor.close()
conn.close()
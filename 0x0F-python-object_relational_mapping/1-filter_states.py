#!/usr/bin/python3
''' lists all states with a name starting with N (upper N)
    from the database hbtn_0e_0_usa'''
import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)
curs = db.cursor()

curs.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id ASC")
res = curs.fetchone()
for row in res:
    print(row)

curs.close()
db.close()

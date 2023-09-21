#!/usr/bin/python3
"""lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa"""

import MySQLdb as database
from sys import argv

if __name__ == '__main__':
    db = database.connect(host="localhost",
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3],
                          port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = %s ORDER BY id", (argv[4],))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

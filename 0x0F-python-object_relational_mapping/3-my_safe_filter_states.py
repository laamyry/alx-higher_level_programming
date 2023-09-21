#!/usr/bin/python3
""" takes in arguments and displays all values"""

import MySQLdb as database
from sys import argv

if __name__ == '__main__':
    db = database.connect(host="localhost",
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3],
                          port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states \
                WHERE name = '{:s}' ORDER BY id ASC;".format(argv[4]))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

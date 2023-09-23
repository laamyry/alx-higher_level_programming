#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import MySQLdb as database
from sys import argv

if __name__ == '__main__':
    db = database.connect(host="localhost",
                          user=argv[1],
                          passwd=argv[2],
                          db=argv[3],
                          port=3306)
    cur = db.cursor()
    cur.execute("""SELECT cities.name
                FROM cities
                INNER JOIN states
                ON states.id = cities.state_id
                WHERE states.name LIKE BINARY '{}'
                ORDER BY cities.id""",).format(argv[4])

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()

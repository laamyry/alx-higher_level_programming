#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    data_base = MySQLdb.connect(
                host="localhost",
                port=3306,
                user=username,
                passwd=password,
                data_base=database)
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id")
    [print(row) for row in cursor.fetchall()]
    cursor.close()
    data_base.close()

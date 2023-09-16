#!/usr/bin/python3
'''lists all states from the database hbtn_0e_0_usa '''
import MySQLdb
import sys

if __name__ == '__main__':
    '''Datebase Access'''
    data_base = MySQLdb.connect(host="localhost",
                         username=sys.argv[1],
                         port=3306,
                         password=sys.argv[2],
                         data_base=sys.argv[3])

    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
    cursor.close()
    data_base.close()

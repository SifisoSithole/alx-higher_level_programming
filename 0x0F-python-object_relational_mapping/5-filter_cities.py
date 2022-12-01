#!/usr/bin/python3

"""This script lists all cities from the database hbtn_0e_4_usa
Arguments:
    0: MySQL username
    1: MySQL password
    2: database: Database
    3: state name
"""
import sys
import MySQLdb

if __name__ == "__main__":
    ls = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=ls[0],
                           passwd=ls[1], db=ls[2])
    cur = conn.cursor()
    cur.execute(f"SELECT cities.name FROM cities LEFT JOIN states ON \
                states.id = cities.state_id WHERE states.name = \
                '{ls[3]}' ORDER BY cities.id ASC")
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i != len(rows) - 1:
            print(rows[i][0], end=', ')
        else:
            print(rows[i][0])

    cur.close()
    conn.close()

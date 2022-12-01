#!/usr/bin/python3

"""This script lists all cities from the database hbtn_0e_4_usa
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
"""

import sys
import MySQLdb

if __name__ == "__main__":
    ls = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=ls[0],
                           passwd=ls[1], db=ls[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities,\
                states WHERE state_id = states.id ORDER BY cities.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()

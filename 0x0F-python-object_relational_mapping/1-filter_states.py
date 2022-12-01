#!/usr/bin/python3

"""This script lists all states with a name starting with N
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    rgu = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=rgu[0],
                           passwd=rgu[1], db=rgu[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    states = cur.fetchall()
    for city in states:
        if city[1][0] == 'N':
            print(city)

    cur.close()
    conn.close()

#!/usr/bin/python3

"""This script lists all states with a name starting with N
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
    3: State to look for in the database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    rgu = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=rgu[0],
                           passwd=rgu[1], db=rgu[2], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY id ASC".format(rgu[3]))
    sts = cur.fetchall()
    for st in sts:
        print(st)
    cur.close()
    conn.close()

#!/usr/bin/python3

"""This script lists all states from the database hbtn_0e_0_usa
Arguments:
    0: MySQL username
    1: MySQL password
    2: Database
"""
import sys
import MySQLdb

if __name__ == "__main__":
    ls = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=ls[1], passwd=ls[2], db=ls[3], charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    st = cur.fetchall()
    for s in st:
        print(s)
    cur.close()
    conn.close()

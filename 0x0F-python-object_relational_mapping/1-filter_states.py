#!/usr/bin/python3
"""
states with a name starting with N
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for stats in cur.fetchall():
        if stats[1][0] == 'N':
            print(stats)
    db.close()

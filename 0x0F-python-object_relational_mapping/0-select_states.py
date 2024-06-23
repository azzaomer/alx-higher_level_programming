#!/usr/bin/python3
"""Lists states"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="127.0.0.1", port=3306, user=argv[1],
    passwd=argv[2], db=argv[3], charset="utf8")
    cur =  conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    query_rows = cur.fetchall()
    for r in query_rows:
        print(r)
    cur.close()
    conn.close()

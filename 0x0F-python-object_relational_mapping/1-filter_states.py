#!/usr/bin/python3
"""Lists all states with a name starting with N (upper N)"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Connecting to database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # Creating cursor
    cur = db.cursor()
    # Executing query
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    # Obtaining query results
    rows = cur.fetchall()
    for row in rows:
        print("(%s, '%s')" % row)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()

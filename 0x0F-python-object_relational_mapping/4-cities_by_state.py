#!/usr/bin/python3
"""Script that lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb


if __name__ == "__main__":
    # Connecting to database
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    # Creating cursor
    cur = db.cursor()
    # Executing query
    cur.execute("""SELECT c.id, c.name, s.name FROM cities c INNER JOIN states s
                ON c.state_id = s.id ORDER BY c.id""")
    # Obtaining query results
    rows = cur.fetchall()
    for cities in rows:
         print("(%s, '%s', '%s')" % cities)

    # Close all cursors
    cur.close()
    # Close all databases
    db.close()

#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

# Connecting to database
db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                     passwd=sys.argv[2], db=sys.argv[3])
# Creating cursor
cur = db.cursor()
# Executing query
nameArg = sys.argv[4]
cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id".format(nameArg))
# Obtaining query results
rows = cur.fetchall()
for row in rows:
    print("(%s, '%s')" % row)
# Close all cursors
cur.close()
# Close all databases
db.close()

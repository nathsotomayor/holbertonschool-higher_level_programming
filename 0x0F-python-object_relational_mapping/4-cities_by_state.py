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
cur.execute("""SELECT * FROM cities c INNER JOIN states s
            ON c.state_id = s.id ORDER BY c.id""")
#print("%s, %s %s" % cur.fetchone())
# Obtaining query results
#rows = cur.fetchall()
rows = db.store_result()
for row in rows.fetch_row(0):
    print(row)
   # print("(%s, '%s', '%s')" % (row,))
# Close all cursors
cur.close()
# Close all databases
db.close()

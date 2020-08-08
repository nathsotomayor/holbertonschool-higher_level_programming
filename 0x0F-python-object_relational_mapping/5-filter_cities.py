#!/usr/bin/python3
"""Script that lists all cities that match with state arg in DB
hbtn_0e_4_usa"""

import sys
import MySQLdb


if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT c.name FROM cities c
                INNER JOIN states s ON c.state_id = s.id
                WHERE BINARY s.name IN ('{}')
                ORDER BY c.id""".format(sys.argv[4]))

    rows = cur.fetchall()
    print(", ".join([cities[0] for cities in rows]))

    cur.close()
    db.close()

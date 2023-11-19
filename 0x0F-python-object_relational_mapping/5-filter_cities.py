#!/usr/bin/env python3

"""
module: 5-filter_cities

Holds function, list_cities()
"""

import MySQLdb
import sys


def list_cities(user_name, passwd, db, state_name):
    """
    A script that takes in the name of a state as an argument and lists all
    cities of that state, using the database hbtn_0e_4_usa
    """
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=passwd,
            db=db,
            port=3306
            )

    cur = db.cursor(MySQLdb.cursors.DictCursor)

    query = "SELECT cities.name FROM cities JOIN states ON cities.state_id = "
    query += "states.id WHERE states.name = %s ORDER BY cities.id ASC"

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    i = 1  # Loop counter

    for state in rows:
        if i < len(rows):
            print(state['name'], end=", ")
        else:
            print(state['name'])
        i += 1

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    list_cities(uname, passwd, db, state_name)

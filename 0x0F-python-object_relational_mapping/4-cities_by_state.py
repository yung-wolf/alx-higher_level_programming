#!/usr/bin/env python3

"""
module: 4-cities_by_state
has one function, print_city_name()
"""

import MySQLdb
import sys


def print_city_name(user_name, passwd, db):
    """
    List all cities from the database hbtn_0e_4_usa
    """
    # connect to database (db)
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=passwd,
            db=db,
            port=3306
            )

    # create cursor
    cur = db.cursor()

    # write query
    query = "SELECT cities.id, cities.name, states.name FROM cities JOIN "
    query += "states ON cities.state_id = states.id ORDER BY cities.id ASC"

    # exe query
    cur.execute(query)

    # print result
    for state in cur:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    print_city_name(uname, passwd, db)

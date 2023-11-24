#!/usr/bin/python3

"""
Module: holds one function, print_states_n()
"""

import MySQLdb
import sys


def print_states_n(user_name, passwd, db):
    """ lists all states with a name starting with N."""
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=passwd,
            db=db,
            port=3306
            )

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name "
                "LIKE 'N%' ORDER BY states.id ASC")

    for state in cur:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    print_states_n(uname, passwd, db)

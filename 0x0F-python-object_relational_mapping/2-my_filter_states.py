#!/usr/bin/ python3

"""
module: has one function, print_state_name()
"""

import MySQLdb
import sys


def print_state_name(user_name, passwd, db, state_name):
    """
    displays all values in the states table of hbtn_0e_0_usa
    where name matches the argument.

    argument:
        state_name
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
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC"
    f_query = query.format(state_name)

    # exe query
    cur.execute(f_query)

    # print result
    for state in cur:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    print_state_name(uname, passwd, db, state_name)

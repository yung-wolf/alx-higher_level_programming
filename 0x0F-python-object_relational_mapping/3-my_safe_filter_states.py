#!/usr/bin/python3

"""
module: 3-my_safe_filter_states

Holds function, safe_print_state()
"""

import MySQLdb
import sys


def safe_print_state(user_name, passwd, db, state_name):
    """A script that takes in arguments and displays all values in the states
    table of hbtn_0e_0_usa where name matches the argument. But this tim,
    one that is safe from MySQL injections!
    """
    db = MySQLdb.connect(
            host="localhost",
            user=user_name,
            passwd=passwd,
            db=db,
            port=3306
            )

    cur = db.cursor(MySQLdb.cursors.DictCursor)

    query = "SELECT * FROM states WHERE name = %s ORDER BY states.id ASC"

    cur.execute(query, (state_name,))

    for state in cur:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]
    state_name = sys.argv[4]

    safe_print_state(uname, passwd, db, state_name)

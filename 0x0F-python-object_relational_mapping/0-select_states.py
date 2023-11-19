#!/usr/bin/env python3

"""
module: A script that list all states from database `hbtn_0e_0_usa`
"""

import MySQLdb
import sys


def print_states(u_name, passwd, db):
    """List all states from `hbtn_0e_0_usa` db"""
    db = MySQLdb.connect(
        host="localhost",
        user=u_name,
        passwd=passwd,
        db=db,
        port=3306
    )

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    for state in cur:
        print(state)

    cur.close()
    db.close()


if __name__ == "__main__":
    uname = sys.argv[1]
    passwd = sys.argv[2]
    db = sys.argv[3]

    print_states(uname, passwd, db)

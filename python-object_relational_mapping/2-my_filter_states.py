#!/usr/bin/python3
"""
2-my_filter_states.py

Displays all values in the states table where name matches
the argument passed.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = db.cursor()

    query = (
        "SELECT id, name FROM states "
        "WHERE name = '{}' "
        "ORDER BY id ASC"
    ).format(state_name)

    cursor.execute(query)

    for row in cursor.fetchall():
        print(row)

    cursor.close()
    db.close()

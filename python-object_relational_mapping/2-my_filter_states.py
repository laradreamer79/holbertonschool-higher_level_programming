#!/usr/bin/python3
"""
2-my_filter_states.py

Displays all values in the states table where name matches
the argument passed (case-sensitive).
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

    query = "SELECT id, name FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    if not rows:
        print(f"No record found matching '{state_name}' (case-sensitive)")
    else:
        for row in rows:
            print(row)

    cursor.close()
    db.close()

#!/usr/bin/python3
"""  lists all states from the database that matches argument """
import sys
import MySQLdb


def filter_states(username, password, database, state_name):
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        user=username,
        passwd=password,
        db=database,
        host='localhost',
        port=3306
    )

    # Create a cursor object for executing SQL queries
    cursor = db.cursor()

    # create the SQL query with the user input and include LIKE BINARY
    query = ("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC"
             .format(state_name))
    cursor.execute(query)

    # Fetch and print all matching rows
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <user> <password> <database> <state>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]
        filter_states(username, password, database, state_name)

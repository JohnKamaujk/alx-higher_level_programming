#!/usr/bin/python3
"""  lists all states from the database that matches argument """
import sys
import MySQLdb


def safe_filter_states(username, password, database, state_name):
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

    # Use parameterized query to fetch data safely
    query = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(query, (state_name,))  # Pass the state_name as a parameter

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
        safe_filter_states(username, password, database, state_name)

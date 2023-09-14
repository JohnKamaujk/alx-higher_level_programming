#!/usr/bin/python3
"""Lists all city names in a specified state from the database."""

import MySQLdb
import sys


def list_city_names_in_state(username, password, database, state_name):
    # Establish a connection to the MySQL database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object for executing SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch city names in the specified state
    query = """
        SELECT cities.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        WHERE states.name = %s
    """
    cursor.execute(query, (state_name,))

    # Fetch and print all city names
    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

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
        list_city_names_in_state(username, password, database, state_name)

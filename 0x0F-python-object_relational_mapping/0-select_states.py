#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


def list_states(username, password, database):
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

    # Execute the SQL query to fetch all states sorted by states.id
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)

    # Fetch all rows and print them
    for state in cursor.fetchall():
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        list_states(username, password, database)

#!/usr/bin/python3
"""Lists all cities with their corresponding states from the database"""
import MySQLdb
import sys


def list_cities_and_states(username, password, database):
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

    # Execute the SQL query to fetch cities with their corresponding states
    query = """SELECT cities.id, cities.name, states.name
               FROM cities
               INNER JOIN states ON states.id = cities.state_id"""
    cursor.execute(query)

    # Fetch and print all city records with their corresponding states
    cities = cursor.fetchall()
    for city in cities:
        print(city)

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
        list_cities_and_states(username, password, database)

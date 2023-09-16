#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_101_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State
from relationship_city import City

if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Database connection parameters
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create the SQLAlchemy engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(username, password, database),
                           pool_pre_ping=True)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects with associated State objects
    cities = session.query(City).order_by(City.id).all()

    # Print the results
    for city in cities:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()

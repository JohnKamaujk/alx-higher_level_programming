#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_14_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python3 script.py <username> <password> <database>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        # Create the database engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query City objects and join with State objects to associate them
        cities_with_states = (session.query(City, State)
                              .join(State).
                              order_by(City.id).all())

        # Print the results in the specified format
        for city, state in cities_with_states:
            print("{}: ({}) {}".format(state.name, city.id, city.name))

        # Close the session
        session.close()

#!/usr/bin/python3
"""Prints the State object with the specified name from the database."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python3 script.py <user> <password> <database> <state>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        # Create the database engine
        engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                               .format(username, password, database),
                               pool_pre_ping=True)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query the State object with the specified name
        state = session.query(State).filter_by(name=state_name).first()

        # Check if the state was found
        if state:
            print(state.id)
        else:
            print("Not found")

        # Close the session
        session.close()

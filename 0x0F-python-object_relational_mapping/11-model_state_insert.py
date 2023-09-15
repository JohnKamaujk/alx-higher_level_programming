#!/usr/bin/python3
"""Adds the State object "Louisiana" to the database hbtn_0e_6_usa."""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

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

        # Create a new State object and add it to the session
        new_state = State(name="Louisiana")
        session.add(new_state)

        # Commit the transaction to save the new state to the database
        session.commit()

        # Print the new state's id
        print(new_state.id)

        # Close the session
        session.close()

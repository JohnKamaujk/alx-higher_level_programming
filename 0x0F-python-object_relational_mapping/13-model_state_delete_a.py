#!/usr/bin/python3
"""Deletes all State objects containing the letter 'a' from the database."""
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

        # Query State objects with names containing the letter 'a'
        states_with_a = (session.query(State)
                         .filter(State.name.like('%a%'))
                         .all())

        # Delete the matching states from the session
        for state in states_with_a:
            session.delete(state)

        # Commit the transaction to save the deletions
        session.commit()

        # Close the session
        session.close()

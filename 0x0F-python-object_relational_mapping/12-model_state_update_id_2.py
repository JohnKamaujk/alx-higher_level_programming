#!/usr/bin/python3
"""Changes the name of a State object in the database hbtn_0e_6_usa."""
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

        # Query the State object with id = 2
        state_to_update = session.query(State).filter_by(id=2).first()

        # Check if the state was found
        if state_to_update:
            # Update the state's name to "New Mexico"
            state_to_update.name = "New Mexico"
            session.commit()  # Commit the transaction to save the update
        else:
            print("Not found")

        # Close the session
        session.close()

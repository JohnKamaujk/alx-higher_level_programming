#!/usr/bin/python3
"""
Script to create the State "California" with the City "San Francisco"
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

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

        # Create all tables
        Base.metadata.create_all(engine)

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a new City object
        new_city = City(name="San Francisco")

        # Create a new State object and associate it with the City
        new_state = State(name="California", cities=[new_city])

        # Add the State and City objects to the session and commit
        session.add(new_state)
        session.add(new_city)
        session.commit()

        # Close the session
        session.close()

#!/usr/bin/python3
"""
14-model_city_fetch_by_state.py

Prints all City objects with their State name.
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
            username, password, database
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = (
        session.query(City, State)
        .join(State)
        .order_by(City.id)
        .all()
    )

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

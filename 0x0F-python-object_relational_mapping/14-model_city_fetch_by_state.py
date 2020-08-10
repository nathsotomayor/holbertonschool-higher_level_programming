#!/usr/bin/python3
"""script that lists all states from a database"""


from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":

        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'
                .format(argv[1], argv[2], argv[3]), pool_pre_ping=True)

        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        session = Session()
        state = session.query(City, State).filter(City.state_id == State.id)
        for s_c, c_c in result:
                print("{}: ({}) {}".format(c_c.name, s_c.id, s_c.name))

        ssesion.close()

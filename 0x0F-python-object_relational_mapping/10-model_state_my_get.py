#!/usr/bin/python3
"""Lists all State objects with the name passed as argument
from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    get_state = session.query(State).filter_by(name=sys.argv[4]).first()
    if get_state is not None:
        print("{}".format(get_state.id))
    else:
        print("Not found")

    session.close()

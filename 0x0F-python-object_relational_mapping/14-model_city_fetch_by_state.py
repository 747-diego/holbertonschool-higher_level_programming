#!/usr/bin/python3
"""write a script that prints all City objects from hbtn_0e_14_usa."""
if __name__ == "__main__":
    from sys import argv as UserInput
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    MyName = UserInput[1]
    MyPassword = UserInput[2]
    MyDataBase = UserInput[3]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MyName, MyPassword, MyDataBase))
    Session = sessionmaker(engine)
    session = Session()

    Record = session.query(City, State).filter(City.state_id == State.id).all()

    for city, state in Record:
        States = state.name
        Cities = city.id
        Name = city.name
        print("{}: ({}) {}".format(States, Cities, Name))

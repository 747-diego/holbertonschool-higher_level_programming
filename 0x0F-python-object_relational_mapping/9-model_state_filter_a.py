#!/usr/bin/python3
"""Write a script that lists all objects that contain the letter a."""
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

    for MyState in session.query(State).order_by(State.id):
        if "a" in MyState.name:
            print("{}: {}".format(MyState.id, MyState.name))

#!/usr/bin/python3
"""Write a script that deletes all State objects with letter a."""
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

    Letter = State.name.contains("a")
    session.query(State).filter(Letter).delete(synchronize_session=False)
    session.commit()

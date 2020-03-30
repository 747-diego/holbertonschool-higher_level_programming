#!/usr/bin/python3
"""Write a script that changes the name of a object from the hbtn_0e_6_usa."""
if __name__ == "__main__":
    from sys import argv as UserInput
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    MyName = UserInput[1]
    MyPassword = UserInput[2]
    MyDataBase = UserInput[3]
    NewId = 2

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MyName, MyPassword, MyDataBase))
    Session = sessionmaker(engine)
    session = Session()

    Id = query(State).filter(State.id == NewId).update({"name": "New Mexico"})
    session.Id
    session.commit()

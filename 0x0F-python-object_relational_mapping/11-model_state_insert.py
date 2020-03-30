#!/usr/bin/python3
"""Write a script that adds the object “Louisiana” to the hbtn_0e_6_usa."""
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

    NewState = State(name='Louisiana')
    session.add(NewState)
    session.commit()
    print(NewState.id)

#!/usr/bin/python3
"""Write a script that prints the object with the name passed as argument."""
if __name__ == "__main__":
    from sys import argv as UserInput
    from model_state import Base, State
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker

    MyName = UserInput[1]
    MyPassword = UserInput[2]
    MyDataBase = UserInput[3]
    MyState = UserInput[4]

    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(MyName, MyPassword, MyDataBase))
    Session = sessionmaker(engine)
    session = Session()

    for My in session.query(State).order_by(State.id):
        if My.name == MyState:
            print(My.id)
        else:
            exit()
    print("Not Found")
    session.close()
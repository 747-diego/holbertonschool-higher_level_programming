#!/usr/bin/python3
"""Write a script that prints first object from database hbtn_0e_6_usa."""
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

    FirstObject = session.query(State).order_by(State.id).first()
<<<<<<< HEAD
=======

>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea
    if FirstObject:
        print("{}: {}".format(FirstObject.id, FirstObject.name))
    else:
        print("Nothing")

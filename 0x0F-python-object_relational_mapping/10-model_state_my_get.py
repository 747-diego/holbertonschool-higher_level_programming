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

    My = session.query(State).filter(State.name == MyState).first()
    if My:
        print(My.id)
    else:
<<<<<<< HEAD
        print("Not Found")
=======
        print("Not found")
>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea

    session.close()

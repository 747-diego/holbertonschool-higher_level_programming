#!/usr/bin/python3
"""Write a script that displays a sereched city."""
if __name__ == "__main__":
    from sys import argv as UserInput
    import MySQLdb

    MyName = UserInput[1]
    MyPassword = UserInput[2]
    MyDataBase = UserInput[3]
    MyState = UserInput[4]

    table = MySQLdb.connect(host="localhost",
                            port=3306,
                            user=MyName,
                            passwd=MyPassword,
                            db=MyDataBase)
    cursor = table.cursor()
<<<<<<< HEAD
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
=======
    cursor.execute("SELECT * FROM states ORDER BY id ASC".format(MyState))
>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea

    for record in cursor.fetchall():
        if record[1] == MyState:
            print(record)
    cursor.close()
    table.close()

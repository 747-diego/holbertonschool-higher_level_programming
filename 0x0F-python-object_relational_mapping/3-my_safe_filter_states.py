#!/usr/bin/python3
"""Write a script that is safe from MySQL injections."""
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
    cursor.execute("SELECT * FROM states\
<<<<<<< HEAD
                   WHERE states.name = '{}'\
                   ORDER BY id ASC".format(MyState))
=======
                   WHERE name=%s\
                   ORDER BY states.id ASC", (MyState, ))
>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea

    for record in cursor.fetchall():
        if record[1] == MyState:
            print(record)
<<<<<<< HEAD
=======

>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea
    cursor.close()
    table.close()

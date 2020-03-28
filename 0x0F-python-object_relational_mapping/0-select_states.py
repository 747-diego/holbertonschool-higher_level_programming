#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa."""
if __name__ == "__main__":
    from sys import argv as UserInput
    import MySQLdb

    MyName = UserInput[1]
    MyPassword = UserInput[2]
    MyDataBase = UserInput[3]

    table = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=MyName,
                         passwd=MyPassword,
                         db=MyDataBase)
    cursor = table.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    for record in cursor.fetchall():
        print(record)
    cursor.close()
    table.close()

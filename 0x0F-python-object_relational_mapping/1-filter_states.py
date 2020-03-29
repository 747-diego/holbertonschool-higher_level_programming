#!/usr/bin/python3
"""Write a script that lists all states with a name starting with N."""
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
        if record[1][0] == "N":
            print(record)
    cursor.close()
    table.close()

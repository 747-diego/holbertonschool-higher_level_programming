#!/usr/bin/python3
"""Write a script that lists all cities from the database hbtn_0e_4_usa."""
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
    cursor.execute("SELECT cities.name\
                   FROM cities\
                   JOIN states ON cities.state_id = states.id\
<<<<<<< HEAD
                   WHERE states.name = %s ORDER BY cities.id ASC", (MyState, ))
=======
                   WHERE states.name = %s ORDER BY cities.id ASC", [MyState])
>>>>>>> 6d048a36da541ad1e8740ae33b16a7809f0588ea

    CityNames = []
    for record in cursor.fetchall():
        CityNames.append(record[0])
    print(", ".join(CityNames))

    cursor.close()
    table.close()

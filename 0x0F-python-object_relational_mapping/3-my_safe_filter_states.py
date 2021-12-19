#!/usr/bin/python3
'''
akes in arguments and displays all values in the states table
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    database = MySQLdb.connect(user=argv[1], passwd=argv[2],
                                database=argv[3])
    createeate = database.cursor()
    createeate.execute("SELECT * from states\
                WHERE name LIKE %s\
                ORDER BY states.id", (argv[4],))
    states = createeate.fetchall()
    for state in states:
        print(state)
    createeate.close()
    database.close()

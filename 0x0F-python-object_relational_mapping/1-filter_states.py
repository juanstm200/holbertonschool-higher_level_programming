#!/usr/bin/python3
'''
lists all states with a name starting with N
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdatabase
    database = MySQLdatabase.connect(user=argv[1], passwd=argv[2],
                                     database=argv[3])
    create = database.cursor()
    create.execute("SELECT * from states\
                WHERE name LIKE 'N%'\
                ORDER BY states.id")
    states = create.fetchall()
    for state in states:
        if state[1][0] == 'N':
            print(state)
    create.close()
    database.close()

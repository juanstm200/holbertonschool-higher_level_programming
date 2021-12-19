#!/usr/bin/python3
'''
Takes in an argument and displays all values in the states table
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    database = MySQLdb.connect(user=argv[1], passwd=argv[2],
                               database=argv[3])
    create = database.cursor()
    create.execute("SELECT * from states\
                WHERE name LIKE '{}' COLLATE latin1_general_cs\
                ORDER BY states.id".format(argv[4]))
    states = create.fetchall()
    for state in states:
        print(state)
    create.close()
    database.close()

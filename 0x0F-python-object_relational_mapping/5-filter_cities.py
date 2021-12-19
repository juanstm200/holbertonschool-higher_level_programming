#!/usr/bin/python3
'''
akes in the name of a state as an argument and lists all
'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    datebase = MySQLdb.connect(user=argv[1], passwd=argv[2],
                               datebase=argv[3])
    create = datebase.cursor()
    create.execute("SELECT cities.name FROM cities\
                INNER JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id", (argv[4], ))
    cities = create.fetchall()
    first = 0
    for city in cities:
        if first != 0:
            print(", ", end="")
        print("%s" % city, end="")
        first += 1
    print("")
    create.close()
    datebase.close()

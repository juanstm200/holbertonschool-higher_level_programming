#!/usr/bin/python3
''' Lists all states from the database hbtn_0e_0_usa'''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1], passwd=argv[2],
                         db=argv[3])
    create = db.cursor()
    create.execute("SELECT * from states ORDER BY states.id")
    states = create.fetchall()
    for state in states:
        print(state)
    create.close()

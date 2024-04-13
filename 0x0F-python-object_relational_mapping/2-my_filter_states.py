#!/usr/bin/python3
'''Filter states by user input '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]

    conx = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                         passwd=db_pass, db=db_name)

    cur = conx.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY '{}'\
             ORDER BY id ASC".format(state_searched))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conx.close()

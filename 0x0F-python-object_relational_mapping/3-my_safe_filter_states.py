#!/usr/bin/python3
'''Filter states by user input '''


if __name__ == '__main__':
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]
    inj_safe = (state_searched,)

    conx = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_pass, db=db_name)

    cur = conx.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY %s\
             ORDER BY id ASC", inj_safe)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conx.close()

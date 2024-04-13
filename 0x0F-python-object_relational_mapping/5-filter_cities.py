#!/usr/bin/python3
'''Safe filter states'''


if __name__ == '__main__':
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_pass = sys.argv[2]
    db_name = sys.argv[3]
    state_searched = sys.argv[4]
    safe_inj = (state_searched,)

    conx = MySQLdb.connect(host="localhost", port=3306, user=db_user,
                           passwd=db_pass, db=db_name)

    cursor = conx.cursor()
    cursor.execute("SELECT name FROM cities WHERE state_id = \
    (SELECT id FROM states WHERE name = %s LIMIT 1)\
          ORDER BY id ASC".format(state_searched), safe_inj)

    rows = cursor.fetchall()

    tupl = []
    for row in rows:
        tupl += row
    print(", ".join(tupl))

    cursor.close()
    conx.close()

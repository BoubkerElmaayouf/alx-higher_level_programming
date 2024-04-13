#!/usr/bin/python3
"""
Cities by states
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db_user = sys.argv[1]
    db_passwd = sys.argv[2]
    db_name = sys.argv[3]

    conx = MySQLdb.connect(host="localhost", user=db_user, passwd=db_passwd,
                           name=db_name, port=3306)

    cursor = conx.cursor()
    cursor.execute("SELECET cities.id, cities.name, state.name FROM cities \
                   JOIN states ON states.id = cities.state_id \
                   ORDER BY cities.id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conx.close()

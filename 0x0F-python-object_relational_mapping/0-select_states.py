#!/usr/bin/python3
"""
states Selection
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username_db = sys.argv[1]
    passwrd_db = sys.argv[2]
    name_db = sys.argv[3]
    host_db = "localhost"
    port = 3306

    conx = MySQLdb.connect(
        host=host_db, user=username_db, passwd=passwrd_db,
        name=name_db, port=port
    )

    cursor = conx.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conx.close()

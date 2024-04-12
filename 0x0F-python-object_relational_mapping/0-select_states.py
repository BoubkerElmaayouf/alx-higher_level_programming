#!/usr/bin/python3
"""
states script
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    username_db = sys.argv[1]
    passwrd_db = sys.argv[2]
    name_db = sys.argv[3]
    port = 3306

    conx = MySQLdb.connect(
        host="localhost", user=username_db, passwrd=passwrd_db,
        name=name_db, port=port
    )

    cursor = conx.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conx.close()

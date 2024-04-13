#!/usr/bin/python3
"""
Filter states module
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    if (sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    conx = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    
    cursor = conx.cursr()
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    conx.close()

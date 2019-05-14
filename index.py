import pymysql

con = pymysql.connect('remotemysql.com', 'g8MjlBGOHf','FMpJJWxnXd','g8MjlBGOHf')

with con:

    cur = con.cursor()
    cur.execute("SELECT * FROM mahasiswa")

    rows = cur.fetchall()

    for row in rows:
        print("{0} {1} {2}".format(row[0], row[1], row[2]))
import pymysql

# Open database connection
db = pymysql.connect('remotemysql.com', 'g8MjlBGOHf','FMpJJWxnXd','g8MjlBGOHf')

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Prepare SQL query to INSERT a record into the database.


try:
   nim=input("nim = ")
   nama=input ("nama:")

   sql = "INSERT INTO mahasiswa (nim, nama) VALUES ('%s', '%s')" %(nim, nama)
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()
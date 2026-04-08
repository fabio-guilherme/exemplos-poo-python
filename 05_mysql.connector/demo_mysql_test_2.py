import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()

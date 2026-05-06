import mysql.connector

# Create Connection
'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password"
)

print(mydb)
'''

#'''
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="password",
  database="mydatabase"
)

mycursor = mydb.cursor()
#'''

# Creating a Database
#mycursor.execute("CREATE DATABASE mydatabase")

# Check if Database Exists
'''
mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)
'''

# Creating a Table
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
#'''
#mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
#'''

#Primary Key
#mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
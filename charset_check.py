import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
  host="localhost",
  user="dvn",
  password="Protivofazaqscgu9",
  database="musicseasi_org.sql"
)

# Get character set of database
mycursor = mydb.cursor()
mycursor.execute("SHOW VARIABLES LIKE 'character_set_database'")
result = mycursor.fetchone()
print("Character set of database:", result[1])
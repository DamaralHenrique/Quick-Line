import mysql.connector as mysql
from mysql.connector import errorcode

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "root",
    passwd = "P@sswordRoot12",
    database = "teste"
)

cursor = db.cursor()

## defining the Query
query = "SELECT * FROM telefone"

## getting records from the table
cursor.execute(query)

## fetching all records from the 'cursor' object
records = cursor.fetchall()

## Showing the data
for record in records:
    print(record)
    print(record[0])
    print(record[1])


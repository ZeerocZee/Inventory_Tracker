import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="inventory_db"
)

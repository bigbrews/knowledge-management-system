import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "BigBrews-23",
    auth_plugin="mysql_native_password",
    database = "episteme_db"
    )

mycursor = db.cursor()

mycursor.execute("SHOW TABLES;")


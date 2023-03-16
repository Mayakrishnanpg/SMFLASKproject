import mysql.connector



DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agricart"
)
CR=DB.cursor(dictionary=True)
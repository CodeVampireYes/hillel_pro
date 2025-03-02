from flask import Flask
import mysql.connector

from db import MySQLHelper

app = Flask(__name__)

db_config = {
    "host": "192.168.100.11",   # или IP сервера MariaDB
    "user": "ar2r",
    "password": "4505",
    "database": "tbotdb"
}

db = MySQLHelper("192.168.100.11", "ar2r", "4505", "tbotdb")
db.connect()

users = db.fetch_all("SELECT * FROM system_metrics")
print(users)

db.disconnect()
@app.route('/')
def show_tables():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]
        conn.close()
        return "<br>".join(tables) if tables else "No tables found."
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(debug=True)

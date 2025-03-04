from flask import Flask, render_template
import mysql.connector

from db import MySQLHelper

app = Flask(__name__)

db_config = {
    "host": "192.168.100.11",   # или IP сервера MariaDB
    "user": "ar2r",
    "password": "4505",
    "database": "tbotdb"
}

db = MySQLHelper("192.168.100.11",
                 "ar2r",
                 "4505",
                 "tbotdb")
db.connect()

users = db.fetch_all("SELECT * FROM users")
print(users)
db.disconnect()


@app.route('/')
def show_tables():
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()

        # Показываем таблицы, а не данные пользователя
        cursor.execute("SHOW TABLES")
        tables = [row[0] for row in cursor.fetchall()]

        conn.close()

        return render_template('index.html', table=tables)
    except Exception as e:
        return f"Error: {str(e)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


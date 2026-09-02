from flask import Flask
import mysql.connector

app = Flask(__name__)


def get_db_connection():
    return mysql.connector.connect(
        host="db",
        user="root",
        password="rootpassword",
        database="devopsdb"
    )


@app.route("/")
def home():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT 'Hello from MySQL!'")
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return f"""
        <h1>Hello from my DevOps Two-Tier Flask App!</h1>
        <p>Database says: {result[0]}</p>
        """

    except Exception as e:
        return f"Database connection error: {e}", 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
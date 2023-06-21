import sqlite3
from flask import Flask, render_template

# Creates database connection and returns it
def get_db_connection():
    # Opens the connection to the database
    conn = sqlite3.connect('database.db')
    # Gives us access to the rows, returns rows in python dictionary form
    conn.row_factory = sqlite3.Row
    return conn

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

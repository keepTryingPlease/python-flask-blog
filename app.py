import sqlite3
from flask import Flask, render_template

app = Flask(__name__)

# Creates database connection and returns it
def get_db_connection():
    # Opens the connection to the database
    conn = sqlite3.connect('database.db')
    # Gives us access to the rows, returns rows in python dictionary form
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    # Open Database connection
    # The database file is made with init_db.py which uses schema.sql to define what the database table will look like
    conn = get_db_connection()
    # This is called an SQL query
    # Selects all entries from the posts table
    # Fetch all fetches all the rows od the query result
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    # posts=posts is an object that's passed as an argument so the index.html template has access to the blog posts
    # render_template is a Flask helper function that allows the use of Jinja templates
    # Junja templates all you to dynamically build HTML pages with Python code
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)

import sqlite3
from flask import Flask, render_template
from werkzeug.exceptions import abort

app = Flask(__name__)

# Creates database connection and returns it
def get_db_connection():
    # Opens the connection to the database
    conn = sqlite3.connect('database.db')
    # Gives us access to the rows, returns rows in python dictionary form
    conn.row_factory = sqlite3.Row
    return conn

def get_post(post_id):
    conn = get_db_connection()
    post = conn.execute('SELECT * FROM posts WHERE id = ?',
                        (post_id,)).fetchone()
    conn.close()
    if post is None:
        abort(404)
    return post

@app.route('/')
def index():
    # Open Database connection
    conn = get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()
    return render_template('index.html', posts=posts)

@app.route('/<int:post_id>')
def post(post_id):
    post = get_post(post_id)
    return render_template('post.html', post=post)

if __name__ == "__main__":
    app.run(debug=True)

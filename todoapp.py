from flask import Flask, render_template, redirect, request, url_for
import sqlite3

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form['task']   # get input from form

        conn = sqlite3.connect('tasks.db')
        cur = conn.cursor()

        cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))

        conn.commit()
        conn.close()

        return redirect(url_for('view_task'))  # go to view page

    return render_template('add.html')

@app.route('/view')
def view_task():
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()

    cur.execute("SELECT * FROM tasks")
    tasks = cur.fetchall()

    conn.close()

    return render_template('view.html', tasks=tasks)

@app.route('/delete/<int:id>')
def delete_task(id):
    conn = sqlite3.connect('tasks.db')
    cur = conn.cursor()

    cur.execute("DELETE FROM tasks WHERE id = ?", (id,))

    conn.commit()
    conn.close()

    return redirect(url_for('view_task'))

def init_db():
    conn = sqlite3.connect('tasks.db')   # create DB file
    cur = conn.cursor()

    cur.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY,
            task TEXT
        )
    ''')

    conn.commit()
    conn.close()



if __name__ == '__main__':
    init_db()
    app.run(debug=True)
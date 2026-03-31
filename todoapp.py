from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add')
def add_task():
    return render_template('add.html')

@app.route('/view')
def view_task():
    return "view working properly"

@app.route('/delete')
def del_task():
    return "del working properly"

if __name__ == '__main__':
    app.run(debug=True)
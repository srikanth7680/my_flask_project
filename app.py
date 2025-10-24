# from flask import Flask

# app = Flask(__name__)

# @app.route("/")
# def home():
#     return "Hello, Flask!"

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Temporary list (we'll add DB later)
tasks = []

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/create', methods=['POST'])
def create():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    task = request.form.get('task')
    if task:
        tasks[task_id] = task
    return redirect(url_for('index'))   

if __name__ == '__main__':
    app.run(debug=True)
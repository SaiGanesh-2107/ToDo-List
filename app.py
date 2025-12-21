from flask import Flask, render_template, request, redirect
import json

app = Flask(__name__)
FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    try:
        with open(FILE, "r") as f:
            return json.load(f)
    except:
        return []

# Save tasks to file
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f)

# Home page
@app.route('/')
def index():
    tasks = load_tasks()
    return render_template("index.html", tasks=tasks)

# Add new task
@app.route('/add', methods=['POST'])
def add_task():
    task_name = request.form['task']
    tasks = load_tasks()
    tasks.append({"name": task_name, "done": False})
    save_tasks(tasks)
    return redirect('/')

# Mark task as done
@app.route('/done/<int:index>')
def mark_done(index):
    tasks = load_tasks()
    tasks[index]['done'] = True
    save_tasks(tasks)
    return redirect('/')

# Delete task
@app.route('/delete/<int:index>')
def delete_task(index):
    tasks = load_tasks()
    tasks.pop(index)
    save_tasks(tasks)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)

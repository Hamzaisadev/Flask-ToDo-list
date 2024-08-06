from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Corrected this line
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    complete = db.Column(db.Boolean)

    def __init__(self, title, complete):
        self.title = title
        self.complete = complete

@app.route('/')
def index():
    todo_list = Todo.query.all()
    print(todo_list)
    return render_template('base.html', todo_list=todo_list)  # Pass todo_list to the template

if __name__ == '__main__':
    with app.app_context():
        print("Importing Todo model...")
        db.create_all()  # Create the table
        print("Table created!") # Check if table creation worked

        new_todo = Todo(title="todo1", complete=False)
        db.session.add(new_todo)
        db.session.commit()
    app.run(debug=True)

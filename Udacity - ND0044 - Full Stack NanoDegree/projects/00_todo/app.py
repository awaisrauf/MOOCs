# server
from flask import Flask, render_template, request, redirect, url_for, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
import sys
from flask_migrate import Migrate


app = Flask(__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost:5432/todoapp'
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# models: create table for todo1
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)
    completed = db.Column(db.Boolean(), nullable=True, default=False)
    list_id  =db.Column(db.Integer, db.ForeignKey('todolists.id'), nullable=False)
    # to represent in better way
    def __repr__(self):
        return f'<Todo {self.id} {self.description}>'


class TodoList(db.Model):
    __tablename__ = 'todolists'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), nullable=False)
    todos = db.relationship('Todo', backref='list', lazy=True)


@app.route('/todos/create', methods=['POST'])
def create_todo():
      description = request.get_json()['description']
      active_list_id = request.get_json()['active_list_id']
      print(active_list_id)
      error  = False
      try:
          todo = Todo(description=description, list_id=active_list_id)
          db.session.add(todo)
          db.session.commit()
          return jsonify({
              'description': todo.description
          })
      except:
          db.session.rollback()
          error = True
          print(sys.exc_info())
      finally:
          db.session.close()
      if error:
          abort(400)


@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def set_completed_todo(todo_id):
    try:
        completed  = request.get_json()['completed']
        print(completed, todo_id)
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return redirect(url_for('index'))


@app.route('/todos/<todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    try:
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        print(Todo.query.get(todo_id))
    except:
        db.session.rollback()
    finally:
        db.session.close()

    return jsonify({'success': True})


@app.route('/lists/<list_id>')
def get_list_todos(list_id):
    return render_template('index.html',
                           todos=Todo.query.filter_by(list_id=list_id).order_by('id').all(),
                           lists = TodoList.query.all(), active_list=TodoList.query.get(list_id))


@app.route('/')
def index():
    return redirect(url_for('get_list_todos', list_id=1))



if __name__ == '__main__':
    app.run()
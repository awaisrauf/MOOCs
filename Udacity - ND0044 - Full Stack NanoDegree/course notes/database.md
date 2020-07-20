### Install following for database in Python
```bash
pip install SQLAlchemy
pip install flask_migrate
pip install
```

### SQLAlchemy in Python: Minmalist Code
```python

from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://<username><password>@localhost:5432/<database_name>'
db = SQLAlchemy(app)
migrate = Migrate(app, db)  # to keep track of versions of database

# Makes a todos table in 
class Todo(db.Model):
  __tablename__ = 'todos'
  id = db.Column(db.Integer, primary_key=True)
  description = db.Column(db.String(), nullable=False)


@app.route('/')
def index():
  return render_template('index.html', data=Todo.query.all())
```
### Adding new record
```python 
todo = Todo(description=description, list_id=active_list_id)
db.session.add(todo)
db.session.commit()
```
### Editing Existing Record
```Python
todo = Todo.query.get(todo_id)
todo.completed = completed    # completed is on of the tables
db.session.commit()
```

### Deleting Existing Record
```Python
todo = Todo.query.get(todo_id)
db.session.delete(todo)
db.session.commit()
```

### Best Coding Practice
First try it, if it fails, rollback and close session no matter what.
```Python
try:
    todo = Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    print(Todo.query.get(todo_id))
except:
    db.session.rollback()
finally:
    db.session.close()
```
### Search Through the Database
```Python
Table.query.one()   # Get one record
Table.query.all()   # Get all the records
Table.query.filter_by(column_name='column_value').first().__dict__ # gives first value where gives values matches in dict form
# search all the shows that will after today
current_time = datetime.datetime.now()
upcoming = Shows.query.filter(Shows.start_time > current_time).all()

```

## Relationships
### One to Many
`db.realationship()` allow sqlalchemy to identify relationship. Should be used in parent table class and referenced in child. **db.relationship() does not setup constraint for foriegn key.**
`backref`: name of parnet in child
`lazy`: how to load parent and child, ahead of time or not for join 
```Python
class Person(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    # parent of Address, Address(first parameter of function) should be name of the childer
    addresses = db.relationship('Address', backref='person', lazy=True)  

class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    # childern configuration
    person_id = db.Column(db.Integer, db.ForeignKey('person.id'), nullable=False)
```

### Resources
1. [Simple Flask Docs For Basic Use](https://flask-sqlalchemy.palletsprojects.com/en/2.x/models/)

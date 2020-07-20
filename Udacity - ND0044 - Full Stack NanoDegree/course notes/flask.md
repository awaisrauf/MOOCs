## Getting Started
#### Installation
```bash
pip install flask
```

#### Run Flask: Option 1 

Add following in the end of your app.py file and run `python app.py`
```python
if __name__ == '__main__':
  app.run(debug=True)
```
#### Run Flask: Option 2
`set FLASK_APP=app.py` (without spaces) to set window variable and then `flask run`
#### Run Flask Option 3
one command
```bash
FLASK_APP=app.py FLASK_DEBUG=true flask
```
#### Development vs Debug Enviornment
To automatically restart app whenever you update code `set FLASK_DEBUG=true`


## Simple Flask App
This code shows a simple flask application with a controller in `app.py`, view `templates/index.html` and model with data structure etc in python file in terms of SQLAlchemy. Overall structure of the app.
![](https://raw.githubusercontent.com/awaisrauf/ComSci-Notes/master/imgs/flaskapp_structure.png?token=AHHDERFQU7DPCUXMKSIFC4S6QSDEO)


`app.py`
```python
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
#todoapp is name of database
app.config ['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:<password>@localhost:5432/todoapp' 
db = SQLAlchemy(app)
migrate = Migrate(app, db)   # tracks changes in structure of data

# models: create table for todo
class Todo(db.Model):
    __tablename__ = 'todos'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String(), nullable=False)

# to get data from view (html) and commit it to database
@app.route('/todos/create', methods=['POST'])
def create_todo():
      description = request.form.get('description')
      todo = Todo(description=description)
      db.session.add(todo)
      db.session.commit()
      return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.all())
```

`templates/index.html`
```HTML
<html>
  <head>
    <title>Todo App</title>
  </head>
  <body>
    <!-- To give data to controller -->
    <form id="form" method="post" action="/todos/create">
      <input type="text" id="description" name="description" />
      <input type="submit" value="Create" />
    </form>
    <!-- To get data from controller -->
    <ul id="todos">
      {% for d in data %}
      <li>{{ d.description }}</li>
      {% endfor %}
    </ul>
  </body>
</html>
```

### Getting Data from HTML to FLASK




## Useful Resources 
1. [Flask Errors](https://flask.palletsprojects.com/en/1.0.x/errorhandling/)
2. [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)


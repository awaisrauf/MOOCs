#### Save or open data into a txt file
```python
# data can be list, dict etc
with open('file_name.txt', 'w') as f:
    print(data, file=f)
```    
Read file 
```python
with open('file.txt', 'r') as f:
    output = f.read()
```    


## Dictionary
Iterate 
```python
for key, value in a_dict.items():
    print(key, '->', value)
```
Getting keys or values as list
```python
dict.keys()
dict.values()
```

## Decorators
Simple decorator
```Python
def print_name(name):
    print(name)
    
def add_greeting(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        print("Hello!")
        return f(*args, **kwargs)
    return wrapper

@add_greeting
def print_name(name):
    print(name)

print_name("sandy")
```
Adding parameter to decorator call
```Python
# first function takes argument for wrapper
def add_greeting(greeting=''):
    def add_greeting_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(greeting)
            return f(*args, **kwargs)
        return wrapper
    return add_greeting_decorator

@add_greeting("what's up!")
def print_name(name):
    print(name)


print_name("kathy")
```
We can also pass information from decorator to function via adding parameter in our functon.
```python
def add_greeting(greeting=''):
    def add_greeting_decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            print(greeting)
            return f(greeting, *args, **kwargs)
        return wrapper
    return add_greeting_decorator

@add_greeting("Yo!")
def print_name(greeting, name):
    print(greeting)
    print(name)
```


## Virtual Enviornment
(Resource](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```bash
# install package
pip install --user virtualenv
# create virtual enviornment
python -m venv env_name   
# activate virtual enviornment
.\env\Scripts\activate
# after activation, all packages will be installed inside this virtual enviornment
# deactivate
deactivate
# export list of all the installed packages
pip freeze
```
*Virtual enviornment creates a folder inside the the project. Should be excluded from version control*

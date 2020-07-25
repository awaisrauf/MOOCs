# Course 5 - Creating Robust Workflows in Python

certificate: [link](https://www.datacamp.com/statement-of-accomplishment/course/65848026d43d28afc8168b9e14a5d10d3212a21b)

## Useful Concepts 
- DRY and WET Code
	- writing reusable functions, one function doing one thing
- using list comprehensions instead of loops
```python 
filenames = ["diabetes.txt", "boston.txt", "iris.txt"]
diabetes, boston, iris = [ Path(os.path.join("data", f)).read_text() for f in filenames]
```
- using generators object: using `()` will make generator object
```python
diabetes, boston, iris = ( Path(os.path.join("data", f)).read_text() for f in filenames)
```
- seperate code into modules and scripts: 
	- modules have reuseable functions and provide tools 
	- scripts are run and perfrom actions by calling fucntions.
	![](imgs/1.png)
- TypeHints can be used to define types of classes and fucntions 
```python
from typing import List, Set, Dict, Tuple, Optional

class TextFile:
	def __init__(self, name: str) -> None:
		self.text = Path(name).read_text()

def get_lines(self) -> List[str]:
	return self.text.split("\n")
```
- Docstrings can be used to descirbe purpose of modules, functions, classes etc. 
- pytest can be use to create tests 
- argparse to give optional varialbes from command line
- gitversion control can be used via api with python (not very useful for me)
- virtual enviornments

```bash
python -m venv .venv
source .venv/Scripts/activate
# For windows
.venv\Scripts\activate
pip freeze > requirements.txt
pip install --requirement requirements.txt

```
- run bash commands from python scripts: subprocesses library
```python
import subprocess

cp = subprocess.run([".venv/Scripts/python", "-m", "pip", "list"], stdout=-1)
for line in cp.stdout.decode().split("\n"):
    print(line)
    if "pandas" in line:
        print(line)
```

- pickle format to store python objects, can also compress and decmpress it.
	- on-the-fly compression/decompression `df.to_pickle('df.pkl.xz')`
	- in pandas: `to_pickle()`, `read_pickle()` 
	- in 

- project tempatels: cookiecutter library

### Rating
Poor 2/10
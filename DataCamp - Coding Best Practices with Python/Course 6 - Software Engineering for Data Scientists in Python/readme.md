# Software Engineering for Data Scientists in Python

About modularity, documentation, & automated testing

- [Course Link](https://www.datacamp.com/courses/software-engineering-for-data-scientists-in-python/user_bookmarks) 
- [Certificate link](https://www.datacamp.com/statement-of-accomplishment/course/d6153779787aaed1fd4d6f5b4d00618336c9fb1d)



## Useful Concepts

- **Modularity:** Write modular code in three stages: modules, classes and functions

- Comments for each type are different: module's comment on top of file, class before `__init__.py` and functions as described below. 

- Follow pep8 conventions to write better code; use`pycodestyle` package or better IDE to test pep8 styling 

- **Package**: A python module follows following structure
  ![](images/2.png)

- Use setup.py and requirements.py to make package portable

  ```python
  # Import needed function from setuptools
  from setuptools import setup
  
  # Create proper setup to be used by pip
  setup(name='text_analyzer',
        version='0.0.1',
        description='Perform and visualize a text anaylsis.',
        author='Awais',
        packages=['text_analyzer'],
        install_requires=['matplotlib==3.0.0'])
  ```

- import functions in `__init__` to access them directly form outside

- a non-public method that you prefer that users don't use should be like `_function_name` according to pep8 conventions. 

- **Class Inheritance **: ![](images/5.png)

  Grand child inheritance, use  `super.__init__(self, var)`

- **Readability**:

  - comment should explain why a line code doing instead of what a line of code doing.
    ![](images/6.png)

  - If ever in doubt about a comment, write it because under-commenting is bigger problem than over-commenting. 

  - Write small functions with descriptive names and one-and-only-one thing to do. 

  - effective use of docstring

    ```python
    def hypotenuse_length(leg_a, leg_b):
        """Find the length of a right triangle's hypotenuse
    
        :param leg_a: length of one leg of triangle
        :param leg_b: length of other leg of triangle
        :return: length of hypotenuse
    
        >>> hypotenuse_length(3, 4)
        5
        """
        return math.sqrt(leg_a**2 + leg_b**2
    ```

- **Testing**: Don't test code in console write tests. 
  Two main ways to test a code

  - `doctest`
    Write small test as an example at the end of docstring like below and use	`doctest.testmode()` to run the test. 

  ```python
  import doctest
  
  def square(num):
      """
      squares given number
      
      :param num: number to be squared
      :return: squraed number
      
      >>> square(5)
      25
      """
      return num**2
  
  doctest.testmod()
  ```

  - `pytest` testing
    
    1. write a file with the name test_name.py and populate it with test like following
   ```python
    from square import square 
    
        def test_square():
            assert square(5)==25
   ```
  
    2. run `pytest` in command line and get results 
  
  - Use `shpinix` to create html from documentation, `Travis CI` for continuous testing, `Codecov` to see test coverage of code, `CodeClimate` to analyze readability 
# Course: Writing Efficient Python Code

This is first course of series [Coding Best Practices with Python](https://learn.datacamp.com/skill-tracks/coding-best-practices-in-python).  

- Course Link: [course](https://learn.datacamp.com/courses/writing-efficient-python-code)
- Certificate Link: [certificate](https://www.datacamp.com/statement-of-accomplishment/course/7c0db4a84731cf2c7d440c0c8d8bcd4b280cfed6)

## Useful Concepts 

### Zen of Python 

- Zen of python is accessable via `import this` and describes best practices for python. 

  ```
  The Zen of Python, by Tim Peters
  
  Beautiful is better than ugly.
  Explicit is better than implicit.
  Simple is better than complex.
  Complex is better than complicated.
  Flat is better than nested.
  Sparse is better than dense.
  Readability counts.
  Special cases aren't special enough to break the rules.
  Although practicality beats purity.
  Errors should never pass silently.
  Unless explicitly silenced.
  In the face of ambiguity, refuse the temptation to guess.
  There should be one-- and preferably only one --obvious way to do it.
  Although that way may not be obvious at first unless you're Dutch.
  Now is better than never.
  Although never is often better than *right* now.
  If the implementation is hard to explain, it's a bad idea.
  If the implementation is easy to explain, it may be a good idea.
  Namespaces are one honking great idea -- let's do more of those!
  ```

  ### Built-in types, functions and modules 

  ![](imgs/1.png
  )

- list of numbers from 1 to 12 with gap of 2 as unpacked list.

  ```python
  list(range(1, 12, 2))
  ```

#### Writing Better/ Efficient Code with built-in functionality

- All of the following have same output 

  ```python
  # Rewrite the for loop to use enumerate
  names = ['Jerry', 'Kramer', 'Elaine', 'George', 'Newman']
  indexed_names = []
  for i, name in enumerate(names):
      index_name = (i, name)
      indexed_names.append(index_name) 
  print(indexed_names)
  
  # Rewrite the above for loop using list comprehension
  indexed_names_comp = [(i, name) for i,name in enumerate(names)]
  print(indexed_names_comp)
  
  # Unpack an enumerate object with a starting index of one
  indexed_names_unpack = [*enumerate(names, 1)]
  print(indexed_names_unpack)
  ```

  ```
  [(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
  [(0, 'Jerry'), (1, 'Kramer'), (2, 'Elaine'), (3, 'George'), (4, 'Newman')]
  [(1, 'Jerry'), (2, 'Kramer'), (3, 'Elaine'), (4, 'George'), (5, 'Newman')]
  
  ```

  
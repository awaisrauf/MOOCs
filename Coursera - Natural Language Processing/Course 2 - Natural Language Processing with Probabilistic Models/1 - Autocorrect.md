# Autocorrect 

- changes miss-spelled words. 

### How it works:

- **Identify a miss-spelled word**

  ```python 
  if word not in vocab:
  	misspelled = True
  ```

- **Find strings n edit distance away**
  edit distance: how many changes we need to make in current word A to make it B. 
  Edits: Insert, Delete, Switch (swaps), replace

- **Filter candidates with dictionary**
  check if n-distance away words are in the dictionary. 
  Edit distance will give many non-word candidates.

- **Calculate word probabilities**
  Calculate probabilities of the word from the corpus i.e. P(w1) = C(w1)/V; where C is count of word in corpus and V is size of vocabulary. 

- 

### Minimum Edit Distance

- Minimum number of edits needed to change a word to another.

  Edits: insert, delete, replace.

  Example: 

  ![](imgs/1.png)

### Minimum Edit Distance Algorithm 

- Dynamic Programming Solution: Convert problems in many short problems and then solve each sub-problem and reusing it for next. 
- Make a box like  following:
  ![](imgs/4.png)
- ![](imgs/2.png)

- To fill any square, use following formula:
  ![](imgs/3.png)

### Interesting Programming Tricks

#### Short circuit
In Python, logical operations such as `and` and `or` have two useful properties. They can operate on lists and they have ['short-circuit' behavior](https://docs.python.org/3/library/stdtypes.html). Try these:

```python
# example of logical operation on lists or sets
print( [] and ["a","b"] )
print( [] or ["a","b"] )
#example of Short circuit behavior
val1 =  ["Most","Likely"] or ["Less","so"] or ["least","of","all"]  # selects first, does not evalute remainder
print(val1)
val2 =  [] or [] or ["least","of","all"] # continues evaluation until there is a non-empty list
print(val2)
```

```shell
[]
['a', 'b']
['Most', 'Likely']
['least', 'of', 'all']
```


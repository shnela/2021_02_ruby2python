# [List Comprehension][]

## Example
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = [f for f in fruits if "a" in f]
assert fruits_with_a == ['apple', 'banana', 'mango']
```

## Syntax
```
newlist = [expression for item in iterable if condition == True]
```

## Other comprehensions

### Dict
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = {f: len(f) for f in fruits if "a" in f}
assert fruits_with_a == {'apple': 5, 'banana': 6, 'mango': 5}
```

### Set
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = {f for f in fruits if "a" in f}
assert fruits_with_a == {'apple', 'banana', 'mango'}
```

### Generator
```python
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
fruits_with_a = (f for f in fruits if "a" in f)
assert list(fruits_with_a) == ['apple', 'banana', 'mango']
```

## Constructing collections
```python
list(), []
...

```

## Exercises
Exercises:
* [measure_words_length.py](measure_words_length.py)
* [count_words.py](count_words.py)

[List Comprehension]: https://www.w3schools.com/python/python_lists_comprehension.asp

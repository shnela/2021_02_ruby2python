#Generators and Itertools

## Generators

```python
def generate_consecutive_n(n):
  for i in range(n):
      yield i

type(generate_consecutive_n)
# <class 'function'>
gen = generate_consecutive_n(3)
type(gen)
# <class 'generator'>
next(gen)
# 0
next(gen)
# 1
next(gen)
# 2
type(gen)
# <class 'generator'>
next(gen)
# StopIteration
next(gen)
# StopIteration
gen = generate_consecutive_n(3)
next(gen)
# 0
list(gen)
# [1, 2]
list(gen)
# []
next(gen)
# StopIteration
```

Exercise: [generators.py](generators.py)

## Itertools
```python
numbers = list(range(10))
even_numbers = numbers[::2]
odd_numbers = numbers[1::2]

assert all(not n % 2 for n in even_numbers)
assert all(n % 2 for n in odd_numbers)
assert not any(n % 2 for n in even_numbers)

# alphabet dict
d = dict(zip('abcd', range(1, 5)))
print(d)
# {'a': 1, 'b': 2, 'c': 3, 'd': 4}

list(zip('abcd', range(1000)))
from itertools import zip_longest
list(zip_longest('abcd', range(1000), fillvalue='-'))
```
[itertools docs](https://docs.python.org/3/library/itertools.html)

[generate_alphabet.py](generate_alphabet.py)
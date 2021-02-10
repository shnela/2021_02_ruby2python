# Container types

## List
```python
# list of only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of only strings
b = ['hello', 'john', 'reese']
print(b)

# list of both integers and strings
c = ['hey', 'you', 1, 2, 3, 'go']
print(c)

# index are 0 based. this will print a single character
print(c[1])  # this will print 'you' in list c

# constructing list
letters = list('some text')
print(letters)
# list is mutable
letters[0] = 's replacement'
print(letters)
```

Let's do [lists_basics.py](./lists_basics.py)

### List [Slicing][]
```python
a[start:stop]  # items start through stop-1
a[start:stop:step]  # items start through stop-1 with step
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array

a[-1]    # last item in the array
a[-2:]   # last two items in the array
a[:-2]   # everything except the last two items

a[::-1]    # all items in the array, reversed
a[1::-1]   # the first two items, reversed
a[:-3:-1]  # the last two items, reversed
a[-3::-1]  # everything except the last two items, reversed
```
Exercise: [slicing.py](./slicing.py)

## Tuple
```python
# tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple types of data.
b = ('hello', 1, 2, 3, 'go')
print(b)  # prints the whole tuple

# index of tuples are also 0 based.
print(b[4])  # this prints a single element in a tuple, in this case 'go'

# constructing tuple
letters = tuple('some text')
print(letters)
# list is mutable
letters[0] = 's replacement'  # Will throw TypeError
```
[muteble_element_in_immutable_tuple.py](muteble_element_in_immutable_tuple.py)

## Dict
```python
# a sample dictionary variable
a = {1:'first name', 2:'last name', 'age':33}
print(a)  # prints the whole dict

# print value having key=1
print(a[1])
# print value having key=2
print(a[2])
# print value having key='age'
print(a['age'])
```

Exercises:
* [measure_words_length.py](measure_words_length.py)
* [count_words.py](count_words.py)

### [dictionaries ordered in Python 3.6+][]
> They are insertion ordered. As of Python 3.6, for the CPython implementation of Python,
> dictionaries remember the order of items inserted.
> This is considered an implementation detail in Python 3.6; you need to use OrderedDict if you want insertion
> ordering that's guaranteed across other implementations of Python (and other ordered behavior).
>
> As of Python 3.7, this is no longer an implementation detail and instead becomes a language feature.

Look at [dict_order.py](./dict_order.py).


## Set
```python

```

[dictionaries ordered in Python 3.6+]: https://stackoverflow.com/a/39980744/1565454
[Slicing]: https://stackoverflow.com/a/509295/1565454

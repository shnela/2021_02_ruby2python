# Container types

## List
```python
# list of having only integers
a = [1, 2, 3, 4, 5, 6]
print(a)

# list of having only strings
b = ['hello', 'john', 'reese']
print(b)

# list of having both integers and strings
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

## Tuple
```python
# tuple having only integer type of data.
a = (1, 2, 3, 4)
print(a)  # prints the whole tuple

# tuple having multiple type of data.
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

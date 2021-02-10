# Python strings and bytes

## String and bytes
```python
unicode_string = 'Łona - ąę'
print(unicode_string)
# Łona - ąę
assert len(unicode_string) == 9
assert type(unicode_string) is str
assert unicode_string[0] == 'Ł'
assert unicode_string[::-1] == 'ęą - anoŁ'

bytes_sequence = unicode_string.encode()
print(bytes_sequence)
# b'\xc5\x81ona - \xc4\x85\xc4\x99'
assert len(bytes_sequence) == 12
assert bytes_sequence[0] == 0xc5  # 197 (int)
```

## Working with files   
[Python open file][]
```python
f = open('output1.txt', 'w')
f.write('Internal of file')
f.close()

# But it's more convenient to skip close
with open('output2.txt', 'w') as f:
    f.write('Internal of file')
```

[Python open file]: https://www.w3schools.com/python/python_file_handling.asp

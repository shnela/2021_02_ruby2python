# Python introduction

## Python version
Check python version in shell.
```shell
python --version  # most often links to deprecated python2
python3 --version
python3 -V
```

## Python vs Ruby
[Ruby vs Python][]

Let's look at the code.
```shell
ls -1 ./python_vs_ruby
> base.py
> base.rb
ruby ./python_vs_ruby/base.rb
> ...
python3 ./python_vs_ruby/base.py
> ...
```

## Run python code
### Interactive interpreter
Run interpreter in terminal by typing `python3`

1. Define two variables `x = 42` and `y = 2`
1. Print `x` and `y`
1. Print `x` `y` times in a loop.

### File
Open file [`0_base.py`](./0_base.py)
1. Reproduce all steps from previous assignment

#### Run in terminal
Run in terminal:
```shell
python3 ./0_base.py
```
Now do the same with `1_datetime.py` and `2_faker.py`.

### External dependencies
```shell
# Create new python environment in '~/.envs/test'
python3 -m venv ~/.envs/test
# Activate environment
source ~/.envs/test/bin/activate
# Now we can use 'python' instead of 'python3'
which python

# install dependencies
pip install faker
# check what's installed
pip freeze
# And run code containing 3rd party libraries
python ./2_faker.py
```

But, what's [PIP][]?
> The Python Package Index (PyPI) is a repository of software for the Python programming language.

Kind of like [RubyGems][]

More info about [Virtual Environments and Packages][]

### Run in pyCharm
[Create and edit run/debug configurations][]

`Right Click on <file name>` &rarr; `Run <file name>`

To set custom environment used by pyCharm go to:
```
File | Settings | Project: ruby2python | Python Interpreter
```
`Right Click on gear` &rarr; `Add...` &rarr; `Existing environment` &rarr; `Path to python executable`

<!--- Links -->
[Ruby vs Python]: https://www.upguard.com/blog/python-vs-ruby
[PIP]: https://pypi.org/
[RubyGems]: https://rubygems.org/
[Virtual Environments and Packages]: https://docs.python.org/3/tutorial/venv.html
[Create and edit run/debug configurations]: https://www.jetbrains.com/help/pycharm/creating-and-editing-run-debug-configurations.html

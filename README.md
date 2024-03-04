# AirBnB clone - The console

Welcome to the AirBnB clone project!

## Learning Objectives

At the end of this project, you are expected to be able to `explain to anyone`, without the help of Google:
- How to create a Python package
- How to create a command interpreter in Python using the `cmd` module
- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a `JSON` file
- How to manage `datetime`
- What is an `UUID`
- What is `*args` and how to use it
- What is `**kwargs` and how to use it
- How to handle named arguments in a function

### 1. How to Create a Python Package

A Python package is a way to organize your Python code into multiple modules, making it more manageable and reusable. Here's a basic way to create a package:

1. `Create a Directory`: This will be your package directory. Name it after your package.
1. `Init File`: Inside this directory, create an `__init__.py` file. This file can be empty but it signals to Python that this directory should be treated as a package.
1. `Add Modules`: Your actual code goes into modules, which are simply Python `.py` files. You can have multiple modules in a package.
1. `Importing Modules`: You can import these modules into other parts of your code using `import` statements.

### 2. Creating a Command Interpreter in Python Using the cmd Module

The `cmd` module in Python provides a simple framework for writing line-oriented command interpreters. Here's a basic structure:
```bash
import cmd

class MyCommandInterpreter(cmd.Cmd):
    prompt = 'myapp> '

    def do_greet(self, line):
        print("Hello!")

    def do_exit(self, line):
        print("Exiting.")
        return True  # Return True to exit the command loop

if __name__ == '__main__':
    MyCommandInterpreter().cmdloop()
```

This code creates a simple command interpreter that responds to `greet` and `exit` commands.

### 3. What is Unit Testing and How to Implement It in a Large Project

Unit testing involves testing individual units or components of a software. In a large project, unit testing ensures that each part of the codebase works correctly. Python's `unittest` framework allows you to define tests for your functions and classes:
```bash
import unittest

class TestMyFunction(unittest.TestCase):
    def test_function(self):
        self.assertEqual(my_function(2, 3), 5)  # Assuming my_function adds two numbers

if __name__ == '__main__':
    unittest.main()
```

For large projects, you can organize tests in a separate directory and run them collectively.

### 4. How to Serialize and Deserialize a Class

Serialization is converting an object into a format that can be stored or transmitted and then reconstructed. Python's `pickle` module can serialize class instances:
```bash
import pickle

class MyClass:
    def __init__(self, name):
        self.name = name

# Serialization
my_object = MyClass("example")
serialized_object = pickle.dumps(my_object)

# Deserialization
deserialized_object = pickle.loads(serialized_object)
```

For JSON serialization, use the `json` module, but remember that it doesn't support custom objects directly without a conversion to a native type (like a dictionary).

### 5. How to Write and Read a JSON File

```bash
import json

# Writing to a JSON file
data = {"name": "John", "age": 30}
with open("data.json", "w") as json_file:
    json.dump(data, json_file)

# Reading from a JSON file
with open("data.json", "r") as json_file:
    data = json.load(json_file)
```

### 6. How to Manage datetime

The `datetime` module in Python helps in manipulating dates and times:
```bash
from datetime import datetime

now = datetime.now()  # Get current date and time
date_string = now.strftime("%Y-%m-%d %H:%M:%S")  # Format as a string
parsed_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")  # Parse from a string
```

### 7. What is an UUID

UUID (Universally Unique Identifier) is a 128-bit number used to uniquely identify information. The `uuid` module in Python can generate UUIDs:
```bash
import uuid

unique_id = uuid.uuid4()  # Generate a random UUID
```

### 8. What is *args and How to Use It

`*args` allows you to pass a variable number of arguments to a function. It's used in function definitions to handle arbitrary numbers of positional arguments:
```bash
def function_with_args(*args):
    for arg in args:
        print(arg)

function_with_args(1, 2, 3)  # Outputs 1, 2, 3
```

### 9. What is **kwargs and How to Use It

`**kwargs` allows you to pass a variable number of keyword arguments to a function. It collects them into a dictionary:
```bash
def function_with_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function_with_kwargs(arg1="value1", arg2="value2")  # Outputs arg1: value1, arg2: value2
```

### 10. How to Handle Named Arguments in a Function

Named arguments (or keyword arguments) are arguments that are passed to a function by explicitly stating the name of the parameter:
```bash
def my_function(arg1, arg2):
    print(arg1, arg2)

my_function(arg1="Hello", arg2="World")  # Prints "Hello World"
```

## More Info / Exemple Shell

### Execution

Your shell should work like this in `interactive mode`:
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash``

## Requirements

### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.7.*)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (``python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the `unittest module`
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: python3 -m unittest discover tests
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

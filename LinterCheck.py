import os, sys  # Multiple imports on one line (style issue) and not used

def add_numbers(x, y):  # No type hints
    return x + y + z  # 'z' is undefined (NameError)

def print_user_info(name: str, age):  # Missing type for age
    print('User:' + name)
    print("Age: %d" % age)  # Improper formatting, could be problematic with non-integers

def do_sensitive():
    password = "123456"  # Hardcoded password (bandit)
    eval("print('Executing something dangerous')")  # Use of eval (security risk)

def UnusedFunction():  # Not called anywhere
    pass

def too_many_arguments(a, b, c, d, e, f, g):  # Too many args (code smell)
    return a + b + c + d + e + f + g

print_user_info("Alice", "25")  # Wrong type: age as string instead of int
print(add_numbers(5, 10))

# ruff check LinterCheck.py --> general
# bandit LinterCheck.py --> security
# flake8 LinterCheck.py --> style
# pylint LinterCheck.py --> Legacy

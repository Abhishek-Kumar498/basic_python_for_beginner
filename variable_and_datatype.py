#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
datatypes_and_variables.py
--------------------------
Demonstrates basic data types and variable usage in Python with clear examples.

Usage:
    $ python datatypes_and_variables.py

Author: sundram kumar
Python Version: 3.6+
"""

# Variables
name = "Alice"
age = 20
height = 5.6

print("Name:", name)
print("Age:", age)
print("Height:", height)

# Basic Data Types
greeting: str = "Hello, World!"
print("\nString Example:", greeting)

number: int = 42
print("Integer Example:", number)

pi: float = 3.14159
print("Float Example:", pi)

complex_num: complex = 2 + 3j
print("Complex Example:", complex_num)

is_active: bool = True
is_logged_in: bool = False
print("Boolean Examples:", is_active, is_logged_in)

# Collection Data Types
fruits: list = ["apple", "banana", "cherry"]
print("\nList Example:", fruits)
fruits.append("mango")
print("Updated List:", fruits)

coordinates: tuple = (10, 20, 30)
print("\nTuple Example:", coordinates)

unique_numbers: set = {1, 2, 3, 3, 4}
print("\nSet Example:", unique_numbers)

student: dict = {
    "name": "Alice",
    "age": 20,
    "grade": "A"
}
print("\nDictionary Example:", student)
print("Student's Name:", student["name"])

# Special Data Type
nothing = None
print("\nNoneType Example:", nothing)

# Multiple Variable Assignment
x, y, z = 10, 20, 30
print("\nMultiple Assignment:", x, y, z)

a = b = c = 100
print("Same Value Assignment:", a, b, c)

# Type Checking
print("\nType of 'greeting':", type(greeting))
print("Type of 'number':", type(number))
print("Type of 'fruits':", type(fruits))
print("Type of 'nothing':", type(nothing))

# Type Conversion
num_str: str = "123"
num_int: int = int(num_str)
num_float: float = float(num_int)
str_again: str = str(num_float)

print("\nType Conversion:")
print("String to Int:", num_int)
print("Int to Float:", num_float)
print("Float to String:", str_again)

# Match-Case Library
### a.k.a. matchcaselib

---

Welcome to matchcaselib, an easy implementation of [Python 3.10's new feature](https://docs.python.org/3/whatsnew/3.10.html) of structural pattern matching.

This project is currently in a **BETA STAGE**.

## Installation
You can install this package by running the following command in your terminal:

`pip install matchcaselib`

or **update it** with the command

`pip install --upgrade matchcaselib`

---

## Usage
```py
from matchcaselib import match

a = input("Enter in a number: ")
a = int(a)
b = input("Enter in another number: ")
b = int(b)

with match(a, b) as m:
  if(m.case(1, 1)):
    print("All ones.")
  if(m.case(1, 2)):
    print("One and two.")
  if(m.case(a, 1)):
    print("The value of A can be anything!  A was {} and b was 1.".format(a))
  if(m.default):
    print("I don't know what you mean...")
```

---

## What you can do:
 - Compare as many sets of variables as you would like (the amount you provide with the initialization of the class must be consistent with the amount you use for the `case` method.)
 - Make a "default" response - Run a block if `default` is true (no matches were found)

## Work in Progress features:
 - Multi-pattern matching (test for multiple patterns)
 - Break function - leave the current match

## What not to do:
 - Use different amounts of variables for the class initialization and the use of the `case` method
 - I don't know, there aren't many bugs right now LOL

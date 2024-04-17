#!/usr/bin/python3
"""defining read_file function"""



def read_file(filename=""):
    """reads filename with UTF8 and print the contents of a UTF8 text to stdout."""
    with open(filename, encoding='utf-8') as f:
        print(f.read(), end="")

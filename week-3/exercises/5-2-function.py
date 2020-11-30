"""
Define a function listNaturalNumbersUpTo():
    Parameters: a number
    Returns: a list containing numbers from 1 to the number (exclusive)
"""


assert listNaturalNumbersUpTo(-1) == []
assert listNaturalNumbersUpTo(0) == []
assert listNaturalNumbersUpTo(1) == [1]
assert listNaturalNumbersUpTo(5) == [1, 2, 3, 4, 5]
print('Tests passed!')

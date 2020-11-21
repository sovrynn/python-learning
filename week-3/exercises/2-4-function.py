"""
Define a function listNaturalNumbersTo():
    Parameters: a number
    Returns: a list containing numbers from 1 to the number (inclusive)
"""


assert listNaturalNumbersTo(-1) == []
assert listNaturalNumbersTo(0) == []
assert listNaturalNumbersTo(1) == [1]
assert listNaturalNumbersTo(5) == [1, 2, 3, 4, 5]
print('Tests passed!')

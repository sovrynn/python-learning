"""
Define a function listNaturalNumbersTo() that takes a number and
    returns a list with numbers from 1 to the number (inclusive).

What should the function return if the number is not positive?
"""


assert listNaturalNumbersTo(-1) == []
assert listNaturalNumbersTo(0) == []
assert listNaturalNumbersTo(1) == [1]
assert listNaturalNumbersTo(5) == [1, 2, 3, 4, 5]
print('Tests passed!')

"""
Define a function printWholeNumbersUpTo() that takes a number and
    prints the whole numbers from 0 to the number (inclusive), separated by spaces,
    with a maximum of 4 numbers on a single line.

If the number is negative, print 'No numbers.'
"""


print('Check the output to see if it\'s correct')

"""
Should print:
No numbers.
"""
printWholeNumbersUpTo(-1)

"""
Should print:
1 2 3
"""
printWholeNumbersUpTo(3)

"""
Should print:
1 2 3 4
5 6 7 8
9 10
"""
printWholeNumbersUpTo(10)

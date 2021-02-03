import util.test as test


"""
Define a function two_greatest():
    Parameters: a list of integers
    Returns: a tuple containing two values:
        First value is the greatest integer in the list (None if there is no greatest integer)
        Second value is the second greatest integer in the list (None if there is no second greatest integer)
"""


test.test_equals(two_greatest([]), (None, None))
test.test_equals(two_greatest([2]), (2, None))
test.test_equals(two_greatest([1, 2]), (2, 1))
test.test_equals(two_greatest([3, 4, 2, 1, 5]), (5, 4))

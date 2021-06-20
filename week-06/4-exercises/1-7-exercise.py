import util.test as test


"""
Define a function nums_greater_than():
    Parameters: a list, an integer
    Returns: a set containing all the numbers in the list greater than the given integer
"""


test.test_equals(nums_greater_than([], 2), set())
test.test_equals(nums_greater_than([1, 2, 3], 2), {3})
test.test_equals(nums_greater_than([1, 2, 3], 0), {1, 2, 3})
test.test_equals(nums_greater_than([1, 2, 3], 4), set())

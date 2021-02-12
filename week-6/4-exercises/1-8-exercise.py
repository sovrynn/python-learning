import util.test as test


"""
Define a function filter_at_steps():
    Parameters: a list, an integer i
    Returns: a list containing every i'th element of the given list, starting at the first element
"""


test.test_equals(filter_at_steps([], 1), [])
test.test_equals(filter_at_steps([1, 2, 3], 1), [1, 2, 3])
test.test_equals(filter_at_steps([1, 2, 3], 2), [1, 3])
test.test_equals(filter_at_steps([1, 2, 3], 3), [1])
test.test_equals(filter_at_steps([2, 4, 6, 8, 10], 2), [2, 6, 10])
test.test_equals(filter_at_steps([2, 4, 6, 8, 10], 3), [2, 8])

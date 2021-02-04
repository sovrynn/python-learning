import util.test as test


"""
Define a function max_of_list():
    Parameters: a list of integers
    Returns: the largest integer in the list (None if the list is empty)
"""


test.test_equals(max_of_list([]), None)
test.test_equals(max_of_list([1]), 1)
test.test_equals(max_of_list([1,3]), 3)
test.test_equals(max_of_list([-1, -2, 5, 1]), 5)
test.test_equals(max_of_list([-1, -2, -3]), -1)

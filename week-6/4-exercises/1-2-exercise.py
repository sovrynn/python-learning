import util.test as test


"""
Define a function index_of_max_of_list():
    Parameters: a list of integers
    Returns: the index of the largest integer in the list (-1 if the list is empty)
"""


test.test_equals(index_of_max_of_list([]), -1)
test.test_equals(index_of_max_of_list([1]), 0)
test.test_equals(index_of_max_of_list([1,3]), 1)
test.test_equals(index_of_max_of_list([-1, -2, 5, 1]), 2)
test.test_equals(index_of_max_of_list([-1, -2, -3]), 0)

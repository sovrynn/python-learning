import util.test as test


"""
Define a function index_of_max_in_2d_list():
    Parameters: a 2D list of integers
    Returns: a tuple containing the indexes of the greatest number in the 2D list (None if empty)
"""


test.test_equals(index_of_max_in_2d_list([[]]), None)
test.test_equals(index_of_max_in_2nd_list([[1]]), (0, 0))
test.test_equals(index_of_max_in_2d_list([[1, 2], [3, 4]]), (1, 1))
test.test_equals(index_of_max_in_2d_list([[1, 4], [3, 2]]), (0, 1))

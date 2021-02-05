import util.test as test


"""
Define a function num_occurrences():
    Parameters: a 2D list, an integer
    Returns: the number of times the given integer occurs in the 2D list
"""


test.test_equals(num_occurrences([[]], 0), 0)
test.test_equals(num_occurrences([[1, 2], [3, 4]], 2), 1)
test.test_equals(num_occurrences([[1, 2], [3, 4]], 5), 0)
test.test_equals(num_occurrences([[1, 7], [2, 7], [3, 7]], 7), 3)

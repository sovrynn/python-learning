import util.test as test


"""
Define a function get_counts():
    Parameters: a list of integers
    Returns: a dict which contains key-value pairs such that:
        a key is a number in the list, and its value is the number of times that number occured in the list
"""


test.test_equals(get_counts([]), {})
test.test_equals(get_counts([2]), {2: 1})
test.test_equals(get_counts([3, 6]), {3: 1, 6: 1})
test.test_equals(get_counts([2, 2, 4, 4, 4, 6]), {2: 2, 4: 3, 6: 1})

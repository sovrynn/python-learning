import util.test as test


"""
Define a function filter_greater_than():
    Parameters: a list and an integer
    Returns: a list containing only the elements of the original list that are greater
        than the given integer
"""
# Start of your code

# End of your code


test.test_equals(filter_greater_than([-1, 0, 5, 7, 10], 6), [7, 10])
test.test_equals(filter_greater_than([1, 2], 0), [1, 2])

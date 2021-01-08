import util.test as test


"""
Define a function get_unique_elements():
    Parameters: a list
    Returns: a set containing the unique elements of the given list 
"""
# Start of your code

# End of your code


test.test_equals(get_unique_elements([1, 1]), {1})
test.test_equals(get_unique_elements([1, 1, 2, 3]), {1, 2, 3})
test.test_equals(get_unique_elements([1, 2, 2]), {1, 2})

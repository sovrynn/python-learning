import util.test as test


"""
Define a function contains_none():
    Parameters: a 2D list
    Returns: True if the 2D list None as an element in a row, False otherwise 
"""
# Start of your code

# End of your code


test.test_equals(contains_none([[0]]), False)
test.test_equals(contains_none([[None]]), True)
test.test_equals(contains_none([[0, 1, 2], [4, None, 4], [1, 6, 7]]), True)
test.test_equals(contains_none([[1, 2, 3], [4, 5, 6], [7, 7, 7]]), False)

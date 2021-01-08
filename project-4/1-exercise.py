import util.test as test


"""
Define a function exists_triple_row():
    Parameters: a 2D list that is 3 columns wide
    Returns: True if there is a row with 3 of the same element, False otherwise
"""
# Start of your code

# End of your code


# Single row
test.test_equals(exists_triple_row([[0, 0, 0]]), True)
test.test_equals(exists_triple_row([[0, 0, 1]]), False)

# Triple exists
test.test_equals(exists_triple_row([[0, 0, 0], [1, 2, 3], [4, 5, 6]]), True)
test.test_equals(exists_triple_row([[0, 1, 2], [4, 4, 4], [5, 6, 7]]), True)
test.test_equals(exists_triple_row([[1, 2, 3], [4, 5, 6], [7, 7, 7]]), True)

# Triple does not exist
test.test_equals(exists_triple_row([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), False)
test.test_equals(exists_triple_row([[0, 0, 1], [2, 3, 4], [5, 6, 7]]), False)

# Triple does not exist, tricky
test.test_equals(exists_triple_row([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), False)
test.test_equals(exists_triple_row([[0, 0, 1], [0, 0, 1], [0, 0, 1]]), False)

import util.test as test


"""
Define a function exists_triple():
    Parameters: a 3x3 2D list
    Returns: True if there is a row, column, or diagonal with 3 of the same element, False otherwise
"""
# Start of your code

# End of your code


# Triple row exists
test.test_equals(exists_triple([[0, 0, 0], [1, 2, 3], [4, 5, 6]]), True)
test.test_equals(exists_triple([[0, 1, 2], [4, 4, 4], [5, 6, 7]]), True)
test.test_equals(exists_triple([[1, 2, 3], [4, 5, 6], [7, 7, 7]]), True)

# Triple column exists
test.test_equals(exists_triple([[0, 1, 2], [0, 3, 4], [0, 5, 6]]), True)
test.test_equals(exists_triple([[0, 1, 2], [3, 1, 4], [5, 1, 6]]), True)
test.test_equals(exists_triple([[1, 2, 0], [3, 4, 0], [5, 6, 0]]), True)

# Triple diagonal exists
test.test_equals(exists_triple([[0, 1, 2], [3, 0, 4], [5, 6, 0]]), True)
test.test_equals(exists_triple([[1, 2, 0], [3, 0, 4], [0, 5, 6]]), True)

# No triple exists
test.test_equals(exists_triple([[0, 1, 2], [3, 4, 5], [6, 7, 8]]), False)
test.test_equals(exists_triple([[0, 0, 1], [2, 3, 4], [5, 6, 7]]), False)

# Triple exists, tricky
test.test_equals(exists_triple([[0, 0, 1], [1, 0, 0], [0, 1, 0]]), True)
test.test_equals(exists_triple([[0, 1, 0], [1, 0, 1], [0, 1, 0]]), True)
test.test_equals(exists_triple([[0, 0, 1], [0, 0, 1], [1, 1, 1]]), True)
test.test_equals(exists_triple([[0, 0, 1], [0, 0, 1], [1, 1, 0]]), True)

# No triple exists, tricky
test.test_equals(exists_triple([[1, 1, 0], [0, 0, 1], [1, 1, 0]]), False)

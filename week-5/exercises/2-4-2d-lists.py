import util.test as test


"""
Define a function num_elements():
    Parameters: a 2D list
    Returns: The number of elements in the 2D list. In other words, the sum of the number of elements in each list
        in the 2D list.
"""
# Start of your code

# End of your code


test.test_equals(num_elements([["a", "b"], ["c", "d"]]), 4)
test.test_equals(num_elements([[1, 2], ["a", "b", 3]]), 5)
test.test_equals(num_elements([[1]]), 1)
test.test_equals(num_elements([[1], [2, 3], [4, 5, 6]]), 6)

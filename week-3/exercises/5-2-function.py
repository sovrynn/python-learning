import util.test as test


"""
Define a function list_natural_numbers_up_to():
    Parameters: an integer
    Returns: a list containing all integers from 1 to the integer (exclusive)
"""
# Start of your code

# End of your code


test.test_equals(list_natural_numbers_up_to(-1), [])
test.test_equals(list_natural_numbers_up_to(0), [])
test.test_equals(list_natural_numbers_up_to(2), [1])
test.test_equals(list_natural_numbers_up_to(5), [1, 2, 3, 4])

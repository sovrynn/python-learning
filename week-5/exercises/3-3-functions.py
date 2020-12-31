import util.test as test


def mystery_func(num):
    return num * 31 + num


"""
Define a function add_mystery_func_results():
    Parameters: two ints
    Returns: the sum of calling mystery_func() on each int
"""
# Start of your code

# End of your code


test.test_equals(add_mystery_func_results(1, 2), mystery_func(1) + mystery_func(2))
test.test_equals(add_mystery_func_results(2, 3), mystery_func(2) + mystery_func(3))
test.test_equals(add_mystery_func_results(4, 11), mystery_func(4) + mystery_func(11))

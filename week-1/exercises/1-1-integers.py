import util.test as test


def mystery_func(x, y, z):
    """
    Parameters: integers x, y, z
    Returns: the sum of the first two integers, multiplied by the third integer
    """
    # Start of your code
    return None
    # End of your code


test.test_equals(mystery_func(1, 2, 3), 9)
test.test_equals(mystery_func(-1, -1, 0), 0)
test.test_equals(mystery_func(3, 4, -2), -14)

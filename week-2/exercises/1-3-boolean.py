import util.test as test


def only_one_is_true(a, b):
    """
    Parameters: booleans a, b
    Returns:
        True if exactly one of a or b is True
        False otherwise
    """
    # Start of your code
    return None
    # End of your code


test.test_equals(only_one_is_true(True, False), True)
test.test_equals(only_one_is_true(False, True), True)
test.test_equals(only_one_is_true(True, True), False)
test.test_equals(only_one_is_true(False, False), False)

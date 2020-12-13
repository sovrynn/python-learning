import util.test as test


def a_true_b_false(a, b):
    """
    Parameters: booleans a, b
    Returns:
        True if a is True and b is False
        False otherwise
    """
    # Start of your code
    return None
    # End of your code


test.test_equals(a_true_b_false(True, False), True)
test.test_equals(a_true_b_false(False, True), False)
test.test_equals(a_true_b_false(True, True), False)
test.test_equals(a_true_b_false(False, False), False)

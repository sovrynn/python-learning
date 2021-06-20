import util.test as test


def pairs_are_equal(a, b, c, d):
    """
    Parameters: booleans a, b, c, d
    Returns:
        True if a, b are equal and c, d are equal
        False otherwise
    """
    # Start of your code
    return None
    # End of your code


test.test_equals(pairs_are_equal(True, True, False, False), True)
test.test_equals(pairs_are_equal(True, True, True, True), True)
test.test_equals(pairs_are_equal(False, False, False, False), True)
test.test_equals(pairs_are_equal(False, False, True, True), True)
test.test_equals(pairs_are_equal(True, False, True, True), False)
test.test_equals(pairs_are_equal(False, True, True, True), False)
test.test_equals(pairs_are_equal(False, False, True, False), False)
test.test_equals(pairs_are_equal(False, False, False, True), False)

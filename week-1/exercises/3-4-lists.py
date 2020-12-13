import util.test as test


def remove_first_two_and_last_two(l):
    """
    Parameters: list l
    Returns: a list formed by removing the first two and last two elements of l
    """
    # Start of your code
    return None
    # End of your code


test.test_equals(remove_first_two_and_last_two([1, 2, 3, 4, 5, 6]), [3, 4])
test.test_equals(remove_first_two_and_last_two([1, 2, 3, 4]), [])
test.test_equals(remove_first_two_and_last_two([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), [3, 4, 5, 6, 7, 8])

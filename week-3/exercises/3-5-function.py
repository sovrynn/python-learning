import util.test as test


"""
Define a function compare_lengths():
    Parameters: two strings
    Returns:
        'greater' if the first string has greater length than the second string
        'equal' if the two strings have equal lengths
        'smaller' if the first string has smaller length than the second string
"""
# Start of your code

# End of your code


test.test_equals(compare_lengths('abc', 'a'), 'greater')
test.test_equals(compare_lengths('a', 'b'), 'equal')
test.test_equals(compare_lengths('a', 'abc'), 'smaller')

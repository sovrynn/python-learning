import util.test as test


"""
Define a function is_matching_parentheses():
    Parameters: a string of parentheses
    Returns: True if the parentheses are correctly matching, False otherwise
"""
# Start of your code

# End of your code


test.test_equals(is_matching_parentheses(')('), False)
test.test_equals(is_matching_parentheses('()('), False)
test.test_equals(is_matching_parentheses('('), False)
test.test_equals(is_matching_parentheses('())('), False)

test.test_equals(is_matching_parentheses(''), True)
test.test_equals(is_matching_parentheses('()'), True)
test.test_equals(is_matching_parentheses('(()())'), True)
test.test_equals(is_matching_parentheses('()()'), True)
test.test_equals(is_matching_parentheses('(())'), True)


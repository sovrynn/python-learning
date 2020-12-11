import util.test as test


"""
Define a function filter_longer_than_two():
    Parameters: a list (of strings)
    Returns: a list containing only the strings of the original list that have length
        greater than two
"""
# Start of your code

# End of your code


test.test_equals(filter_longer_than_two([]), [])
test.test_equals(filter_longer_than_two(["", "1", "12", "123", "1234"]), ["123", "1234"])
test.test_equals(filter_longer_than_two(["abc", "123"]), ["abc", "123"])

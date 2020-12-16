import util.test as test


"""
Write a function double():
    Parameters: an integer
    Returns: double the integer
"""


test.test_equals(double(0), 0)
test.test_equals(double(1), 2)
test.test_equals(double(3), 6)


"""
Write a function print_double_one_to_five():
    Parameters: N/A
    Side Effect: prints the result of calling double() on each integer
        from 1 to 5
    Returns: N/A
"""


"""
Expected output:
2
4
6
8
10
"""
print_double_one_to_five()


"""
Write a function print_double_one_to():
    Parameters: an integer
    Side Effect: prints the result of calling double() on each integer
        from 1 to the given integer
    Returns: N/A
"""


"""
Expected output:
2
4
6
"""
print_double_one_to()

def onlyOneIsTrue(a, b):
    """
    Parameters: booleans a,b
    Returns:
        True if exactly one of a,b is True
        False otherwise
    """
    # Start of your code
    return True
    # End of your code


assert onlyOneIsTrue(True, False)
assert onlyOneIsTrue(False, True)
assert not onlyOneIsTrue(True, True)
assert not onlyOneIsTrue(False, False)
print('Tests passed!')
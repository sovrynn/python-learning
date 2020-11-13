def pairsAreEqual(a, b, c, d):
    """
    Parameters: booleans a,b,c,d
    Returns:
        True if a,b are equal and c,d are equal
        False otherwise
    """
    # Start of your code
    return True
    # End of your code


assert pairsAreEqual(True, True, False, False)
assert pairsAreEqual(True, True, True, True)
assert pairsAreEqual(False, False, False, False)
assert pairsAreEqual(False, False, False, False)
assert not pairsAreEqual(True, False, True, True)
assert not pairsAreEqual(True, True, True, False)
assert not pairsAreEqual(True, False, True, False)
print('Tests passed!')
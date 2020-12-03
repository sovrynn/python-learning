"""
Define a function compareLengths():
    Parameters: two strings
    Returns:
        'greater' if the first string has greater length than the second string
        'equal' if the two strings have equal lengths
        'smaller' if the first string has smaller length than the second string
"""


assert compareLengths('a', 'b') == 'equal'
assert compareLengths('abc', 'a') == 'greater'
assert compareLengths('a', 'abc') == 'smaller'
print('Tests passed!')

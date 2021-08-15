from linked_list_utils import *
import util.test as test


"""
Define a function linked_list_contains():
    Parameters: a linked list, a value
    Returns: True if the linked list contains the value, False otherwise
"""
# Start of your code

# End of your code


list = construct_linked_list([3])
test.test_equals(linked_list_contains(list, 1), False)
test.test_equals(linked_list_contains(list, 3), True)

list = construct_linked_list([-1, 3, 5])
test.test_equals(linked_list_contains(list, -2), False)
test.test_equals(linked_list_contains(list, -1), True)
test.test_equals(linked_list_contains(list, 0), False)
test.test_equals(linked_list_contains(list, 3), True)
test.test_equals(linked_list_contains(list, 4), False)
test.test_equals(linked_list_contains(list, 5), True)


from linked_list_utils import *
import util.test as test


"""
Define a function linked_list_append():
    Parameters: a linked list, a value
    Side Effect: appends the value to the linked list
    Returns: N/A
"""
# Start of your code

# End of your code


list = construct_linked_list([1])
linked_list_append(list, 2)
test.test_equals(test_linked_list_equals(list, [1, 2]), True)

list = construct_linked_list([1, 3, 5])
linked_list_append(list, 7)
test.test_equals(test_linked_list_equals(list, [1, 3, 5, 7]), True)


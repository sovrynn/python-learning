from linked_list_utils import *
import util.test as test


"""
Define a function linked_list_delete():
    Parameters: a linked list, a value
    Side Effect: deletes the value from the linked list, if it exists
    Returns: N/A
"""
# Start of your code

# End of your code


list = construct_linked_list([1, 2])
linked_list_delete(list, 2)
test.test_equals(test_linked_list_equals(list, [1]), True)

list = construct_linked_list([1, 2])
linked_list_delete(list, 1)
test.test_equals(test_linked_list_equals(list, [2]), True)

list = construct_linked_list([1, 3, 5])
linked_list_delete(list, 3)
test.test_equals(test_linked_list_equals(list, [1, 5]), True)


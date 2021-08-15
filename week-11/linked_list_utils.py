class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def construct_linked_list(vals):
    if vals == []:
        return None
    node = Node(vals[0])
    node.next = construct_linked_list(vals[1:])
    return node


def test_linked_list_equals(node, vals):
    if node == None:
        return vals == []
    return not vals == [] and node.data == vals[0] and test_linked_list_equals(node.next, vals[1:])


from typing import Optional


class Node:
    def __init__(self, value, left_child: (Optional['Node']), right_child: (Optional['Node'])):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value


def create_tree():
    node1 = Node(37, None, None)
    node2 = Node(35, None, node1)
    node3 = Node(51, None, None)
    node4 = Node(93, None, None)
    node5 = Node(47, node2, node3)
    node6 = Node(73, None, None)
    node7 = Node(99, node4, None)
    node8 = Node(58, node5, None)
    node9 = Node(88, node6, node7)
    head = Node(62, node8, node9)
    return head

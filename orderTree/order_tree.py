import time
from typing import List
from tree import Node, create_tree


def preorder1(head: Node, store: list):
    if head is None:
        return
    store.append(head.value)
    preorder1(head.left_child, store)
    preorder1(head.right_child, store)


def preorder2(head: Node) -> list:
    def lc(head: Node, store: list, result: list):
        if head is None:
            return
        result.append(head.value)
        store.append(head)
        lc(head.left_child, store, result)

    if head is None:
        return []
    result = []
    store = []
    lc(head, store, result)

    while len(store) != 0:
        temp = store.pop()
        lc(temp.right_child, store, result)
    return result


def inorder1(head: Node, store: list):
    if head is None:
        return
    inorder1(head.left_child, store)
    store.append(head.value)
    inorder1(head.right_child, store)


def inorder2(head: Node):
    def lc(head: Node, store: list):
        while head is not None:
            store.append(head)
            head = head.left_child

    if head is None:
        return []
    store = []
    result = []
    lc(head, store)
    while len(store) != 0:
        head = store.pop()
        result.append(head.value)
        lc(head.right_child, store)
    return result


def postorder1(head: Node, store: list):
    if head is None:
        return
    postorder1(head.left_child, store)
    postorder1(head.right_child, store)
    store.append(head.value)


def postorder2(head: Node):
    def lc(head: Node, store: list):
        while head is not None:
            store.append(head)
            head = head.left_child

    if head is None:
        return []
    store = []
    result = []
    lc(head, store)
    prev = None
    while len(store) != 0:
        temp = store[-1]
        if temp.right_child is not None and prev is not store[-1].right_child:
            lc(temp.right_child, store)
        else:
            result.append(store[-1].value)
            prev = store.pop()
    return result


def levelorder1(nodes: List[Node], result: list):
    if len(nodes) == 0:
        return
    next_leval_nodes = []
    for node in nodes:
        result.append(node.value)
        if node.left_child is not None:
            next_leval_nodes.append(node.left_child)
        if node.right_child is not None:
            next_leval_nodes.append(node.right_child)
    levelorder1(next_leval_nodes, result)


def levelorder2(head: Node):
    if head is None:
        return []
    store = [head]
    result = [head.value]
    while store:
        temp_store = []
        for node in store:
            if node.left_child is not None:
                temp_store.append(node.left_child)
                result.append(node.left_child.value)
            if node.right_child is not None:
                temp_store.append(node.right_child)
                result.append(node.right_child.value)
        store = temp_store
    return result


if __name__ == '__main__':
    head = create_tree()
    result = []
    begin = time.perf_counter()
    preorder1(head, result)
    end = time.perf_counter()
    print('递归先序遍历：', result, '用时', end - begin, sep=' ')
    begin = time.perf_counter()
    result = preorder2(head)
    end = time.perf_counter()
    print('迭代先序遍历：', result, '用时', end - begin, sep=' ')
    result = []
    begin = time.perf_counter()
    inorder1(head, result)
    end = time.perf_counter()
    print('递归中序遍历：', result, '用时', end - begin, sep=' ')
    begin = time.perf_counter()
    result = inorder2(head)
    end = time.perf_counter()
    print('迭代中序遍历：', result, '用时', end - begin, sep=' ')
    result = []
    begin = time.perf_counter()
    postorder1(head, result)
    end = time.perf_counter()
    print('递归后序遍历：', result, '用时', end - begin, sep=' ')
    begin = time.perf_counter()
    result = postorder2(head)
    end = time.perf_counter()
    print('迭代后序遍历：', result, '用时', end - begin, sep=' ')
    result = []
    begin = time.perf_counter()
    levelorder1([head], result)
    end = time.perf_counter()
    print('递归层次遍历：', result, '用时', end - begin, sep=' ')
    begin = time.perf_counter()
    result = levelorder2(head)
    end = time.perf_counter()
    print('迭代层次遍历：', result, '用时', end - begin, sep=' ')

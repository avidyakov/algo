def solution(node):
    while node:
        node.next, node.prev = node.prev, node.next
        if node.prev:
            node = node.prev
        else:
            return node

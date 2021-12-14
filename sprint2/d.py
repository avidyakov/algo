from itertools import count


def solution(node, value):
    for idx in count():
        if node.value == value:
            return idx

        if not node.next_item:
            return -1

        node = node.next_item

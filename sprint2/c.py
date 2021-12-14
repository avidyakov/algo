def solution(node, idx: int):
    if idx:
        head = prev_node = node
        node = node.next_item

        for _ in range(idx - 1):
            prev_node = node
            node = node.next_item

        prev_node.next_item = node.next_item
        return head

    next_item = node.next_item
    node.next_item = None
    return next_item

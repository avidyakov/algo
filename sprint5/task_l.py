def get_children(heap: list, idx: int) -> dict:
    children = {}
    left_idx = idx * 2
    if left_idx < len(heap):
        children[heap[left_idx]] = left_idx

    right_idx = left_idx + 1
    if right_idx < len(heap):
        children[heap[right_idx]] = right_idx

    return children


def sift_down(heap: list, idx: int) -> int:
    """
    >>> sift_down([None, 12, 1, 8, 3, 4, 7], 2)
    5
    """
    children = get_children(heap, idx)
    if not children:
        return idx

    max_child = max(children)

    if max_child <= heap[idx]:
        return idx

    max_child_idx = children[max_child]
    heap[idx], heap[max_child_idx] = heap[max_child_idx], heap[idx]
    return sift_down(heap, max_child_idx)

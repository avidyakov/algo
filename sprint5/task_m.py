def sift_up(heap: list, idx: int) -> int:
    """
    >>> sift_up([None, 12, 6, 8, 3, 15, 7], 5)
    1
    """
    parent_idx = idx // 2
    if parent_idx == 0 or heap[idx] <= heap[parent_idx]:
        return idx

    heap[idx], heap[parent_idx] = heap[parent_idx], heap[idx]
    return sift_up(heap, parent_idx)

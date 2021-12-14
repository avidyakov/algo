def solution(node) -> bool:
    acc = []
    if node.left:
        if node.left.value >= node.value:
            return False

        acc.append(solution(node.left))

    if node.right:
        if node.right.value <= node.value:
            return False

        acc.append(solution(node.right))

    return all(acc)

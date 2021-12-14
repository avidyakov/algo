def get_level(node, level=1):
    if node.left or node.right:
        level += 1

        return max((
            get_level(node.left, level) if node.left else float('-inf'),
            get_level(node.right, level) if node.right else float('-inf')
        ))

    return level


def solution(node) -> bool:
    acc = 0
    if node.left:
        acc += get_level(node.left)

    if node.right:
        acc -= get_level(node.right)

    if not abs(acc) <= 1:
        return False

    if node.left and node.right:
        return all((
            solution(node.left),
            solution(node.right)
        ))

    # if node.left:
    #     return solution(node.left)
    #
    # if node.right:
    #     return solution(node.right)

    return True

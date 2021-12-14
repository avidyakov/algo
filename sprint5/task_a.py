def solution(node) -> int:
    return max({
        node.value,
        solution(node.right) if node.right else float('-inf'),
        solution(node.left) if node.left else float('-inf')
    })

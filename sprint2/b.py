# class Node:
#     def __init__(self, value, next_item=None):
#         self.value = value
#         self.next_item = next_item


def solution(node) -> None:
    print(node.value)

    while node.next_item:
        node = node.next_item
        print(node.value)


# def main():
#     node3 = Node("node3", None)
#     node2 = Node("node2", node3)
#     node1 = Node("node1", node2)
#     node0 = Node("node0", node1)
#     solution(node0)
#
#
# if __name__ == '__main__':
#     main()

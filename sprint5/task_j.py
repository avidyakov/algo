from node import Node


def insert(root, key):
    attr = 'left' if key < root.value else 'right'
    if getattr(root, attr) is None:
        setattr(root, attr, Node(value=key))
        return root

    insert(getattr(root, attr), key)
    return root

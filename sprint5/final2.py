"""ID посылки: 60166233

-- ПРИНЦИП РАБОТЫ --
Программа удаления узла из дерева поиска. Программа находит данный узел в дереве и удаляет его.
На его место ставит другой элемент, чтобы дерево поиска сохраняла свои свойства, если это необходимо.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(h) сколько и требовалось в задании, где h - высота дерева.

Поиск элемента (работает в худшем случае за O(h), но при этим же случае поиск максимального элемента
в левом поддереве или минимального элемента в правом поддереве будет работать за O(1)
т.к. поддеревьев не будет из-за того, что искомый элемент находится в самом низу. И наоборот,
если поиск в лучшем случае будет работать за O(1), если искомый элемент это корень дерева,
то поиск минимального или максимального элемента в поддеревьях будет работать в худшем случае за O(h).

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
1. Поиск элемента в дереве.
O(h), где h - высота дерева из-за того, что это рекурсивный алгоритм.

2. Поиск максимального и минимального элемента
O(1)

"""


def get_max_node(node, parent=None):
    while node.right and node.value <= node.right.value:
        node, parent = node.right, node

    return node, parent


def get_min_node(node, parent=None):
    while node.left and node.value >= node.left.value:
        node, parent = node.left, node

    return node, parent


def remove(head, key):
    if not head:
        pass
    elif head.value < key:
        head.right = remove(head.right, key)
    elif head.value > key:
        head.left = remove(head.left, key)
    elif head.left:
        new_node, parent = get_max_node(head.left)
        if parent:
            parent.right = new_node.left
        else:
            head.left = new_node.left

        new_node.left = head.left
        new_node.right = head.right
        head = new_node
    elif head.right:
        new_node, parent = get_min_node(head.right)
        if parent:
            parent.left = new_node.right
        else:
            head.right = new_node.right

        new_node.left = head.left
        new_node.right = head.right
        head = new_node
    else:
        head = None

    return head

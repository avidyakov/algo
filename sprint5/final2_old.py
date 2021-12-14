"""ID посылки: 59756333

-- ПРИНЦИП РАБОТЫ --
Программа удаления узла из дерева поиска. Программа находит данный узел в дереве и удаляет его.
На его место ставит другой элемент, чтобы дерево поиска сохраняла свои свойства, если это необходимо.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(h) сколько и требовалось в задании, где h - высота дерева.

Поиск элемента (search) работает в худшем случае за O(h), но при этим же случае поиск максимального элемента
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


def search(node, key, _parent=None):
    if node is None:
        return None, None

    if node.value == key:
        return node, _parent

    if node.value > key:
        return search(node.left, key, node)

    return search(node.right, key, node)


def get_max_node(node, parent=None):
    while node.right and node.value <= node.right.value:
        node, parent = node.right, node

    return node, parent


def get_min_node(node, parent=None):
    while node.left and node.value >= node.left.value:
        node, parent = node.left, node

    return node, parent


def remove(head, key):
    searched, searched_parent = search(head, key)
    if searched is None:
        return head

    new_node = None
    if searched.left:
        new_node, new_parent = get_max_node(searched.left)
        if new_parent:
            new_parent.right = new_node.left
        else:
            searched.left = new_node.left

        new_node.left = searched.left
        new_node.right = searched.right

    elif searched.right:
        new_node, new_parent = get_min_node(searched.right)
        if new_parent:
            new_parent.left = new_node.right
        else:
            searched.right = new_node.right

        new_node.left = searched.left
        new_node.right = searched.right

    if searched_parent and searched_parent.left and searched_parent.left.value == key:
        searched_parent.left = new_node
    elif searched_parent and searched_parent.right and searched_parent.right.value == key:
        searched_parent.right = new_node
    else:
        head = new_node

    return head

"""ID успешной посылки: 57422183

-- ПРИНЦИП РАБОТЫ --
Хэш-таблица реализована с помощью класса HashMap. Коллизии разрешаются с помощью метода цепочек. Связанный список
реализован с помощью класса LinkedList. Ключи и значения таблицы - целые числа. Вычисление номера корзины реализовано
с помощью метода умножения, в котором используется только быстрая целочисленная арифметика.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все методы хеш-таблицы работают за O(1) в лучшем случае, а в худшем случае они будут работать за O(n), где n это размер
связанного списка.

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Мы сохраняем в памяти только массив неизменяемой длины n со связанными списками, в которых мы храним ключи и значения
нашей хеш-таблицы. Пространственная сложность нашего алгоритма равна сумме длины этого массива и
множества ключей вместе с их значениями O(n + k).

"""

import sys
import typing
from dataclasses import dataclass


class NodeIterator:

    def __init__(self, current):
        self.current = current

    def __next__(self):
        if self.current:
            result = self.current
            self.current = self.current.next
            return result

        raise StopIteration


@dataclass
class Node:
    key: int
    value: int
    next: typing.Optional['Node'] = None


class LinkedList:

    def __init__(self, head: Node = None):
        self.head = head

    def add(self, key, value):
        self.head = Node(key=key, value=value, next=self.head)

    def remove(self, prev_node):
        if prev_node is None:
            self.head = self.head.next
        else:
            prev_node.next = prev_node.next.next

    def __iter__(self):
        return NodeIterator(self.head)


def get_linked_list(with_idx=False):
    def decorator(func):
        def inner(self, key, *args):
            idx = self._get_bucket_index(key)
            if with_idx:
                return func(self, key, *args, self._values[idx], idx)
            return func(self, key, *args, self._values[idx])

        return inner

    return decorator


class HashMap:

    def __init__(self):
        self.size = 65536
        self._values = [None] * self.size

    @staticmethod
    def _get_bucket_index(key: int) -> int:
        return (key * 2654435769 % 4294967296) >> 16

    @get_linked_list()
    def get(self, key: int, linked_list: typing.Optional[LinkedList]) -> typing.Optional[int]:
        if linked_list is None:
            return

        for node in linked_list:
            if node.key == key:
                return node.value

    @get_linked_list(with_idx=True)
    def put(self, key: int, value: int, linked_list: typing.Optional[LinkedList], idx: int) -> None:
        if linked_list is None:
            linked = LinkedList()
            linked.add(key, value)
            self._values[idx] = linked
            return

        for node in linked_list:
            if node.key == key:
                node.value = value
                return

        linked_list.add(key, value)

    @get_linked_list()
    def delete(self, key: int, linked_list: typing.Optional[LinkedList]) -> typing.Optional[int]:
        if linked_list is None:
            return

        prev = None
        for node in linked_list:
            if node.key == key:
                linked_list.remove(prev)
                return node.value

            prev = node


def main() -> None:
    commands = int(sys.stdin.readline())
    hash_map = HashMap()

    for _ in range(commands):
        command, *args = sys.stdin.readline().split()
        args = map(int, args)
        if command == 'get':
            print(hash_map.get(*args))
        elif command == 'put':
            hash_map.put(*args)
        else:
            print(hash_map.delete(*args))


if __name__ == '__main__':
    main()

import sys
from dataclasses import dataclass


@dataclass
class Node:
    value: int
    next = None


class EmptyQueue(Exception):
    pass


class Queue:

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def push(self, value: int) -> None:
        self._size += 1
        new_node = Node(value=value)
        if self._head is None:
            self._head = self._tail = new_node
        else:
            self._tail.next = new_node
            self._tail = new_node

    def pop(self) -> int:
        if not self._size:
            raise EmptyQueue

        self._size -= 1
        pop_node = self._head
        self._head = self._head.next
        return pop_node.value

    def get_size(self) -> int:
        return self._size


def main():
    number_of_commands = int(sys.stdin.readline().rstrip())
    queue = Queue()
    for _ in range(number_of_commands):
        line = sys.stdin.readline().rstrip()
        if 'put' in line:
            _, value = line.split()
            queue.push(value)
        elif 'get' in line:
            try:
                print(queue.pop())
            except EmptyQueue:
                print('error')
        else:
            print(queue.get_size())


if __name__ == '__main__':
    main()

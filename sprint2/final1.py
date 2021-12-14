"""ID посылки: 53713369

-- ПРИНЦИП РАБОТЫ --
Я реализовал деку на кольцевом буфере с небольшой модификацией. Алгоритм добавления и удаления элементов,
с обратных концов, рассчитывается все с той же головы и хвоста. Только теперь, когда мы добавляем элемент спереди,
мы это делаем по индексу: (head - 1) % max_size. А когда мы удаляем элемент с конца, то делаем это по индексу:
(tail - 1) % max_size.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Все операции push_front, push_back, pop_front, pop_back выполняются за O(1) т.к. дека реализована на кольцевом буфере.

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Пространственная сложность моего алгоритма линейно зависима от максимальной длины деки (n) и равна O(n).
"""

import sys


class EmptyDeque(Exception):
    pass


class ExceededMaximumSize(Exception):
    pass


class DequeOnRingBuffer:

    def __init__(self, max_size: int):
        self._max_size = max_size
        self._buffer = [None] * max_size
        self._size = 0
        self._head = 0
        self._tail = 0

    def _push(self, idx: int, value: int) -> None:
        """Добавляет элемент по индексу"""
        if self._size >= self._max_size:
            raise ExceededMaximumSize

        self._buffer[idx] = value
        self._size += 1

    def push_front(self, value: int) -> None:
        new_head = (self._head - 1) % self._max_size
        self._push(new_head, value)
        self._head = new_head

    def push_back(self, value: int) -> None:
        self._push(self._tail, value)
        self._tail = (self._tail + 1) % self._max_size

    def _pop(self, idx: int) -> int:
        """Извлекает элемент по индексу"""
        if not self._size:
            raise EmptyDeque

        self._size -= 1
        result = self._buffer[idx]
        self._buffer[idx] = None
        return result

    def pop_back(self) -> int:
        new_tail = (self._tail - 1) % self._max_size
        result = self._pop(new_tail)
        self._tail = new_tail
        return result

    def pop_front(self) -> int:
        result = self._pop(self._head)
        self._head = (self._head + 1) % self._max_size
        return result


def main():
    number_of_commands = int(sys.stdin.readline())
    deque_size = int(sys.stdin.readline())
    deque = DequeOnRingBuffer(deque_size)

    for _ in range(number_of_commands):
        line = sys.stdin.readline()
        try:
            if 'push' in line:
                command_name, value = line.split()
                getattr(deque, command_name)(int(value))
            else:
                pop_method = getattr(deque, line.rstrip())
                print(pop_method())
        except (EmptyDeque, ExceededMaximumSize):
            print('error')


if __name__ == '__main__':
    main()

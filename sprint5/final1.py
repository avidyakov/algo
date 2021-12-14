"""ID посылки: 60153591

-- ПРИНЦИП РАБОТЫ --
Пирамидальная сортировка. Сортировка кучей Heap. В функции main мы добавляем элементы по очереди в кучу
и затем достаем по одному элементу из кучи.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
O(n * log(n)) в худшем и лучшем случае.

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Так как куча реализована на массиве, мы используем n дополнительной памяти для хранения n элементов. Сложность равна
O(n)

"""

import sys
import typing


class Heap:
    """Куча"""

    def __init__(self):
        self._values = []

    def add(self, value: typing.Any) -> None:
        self._values.append(value)
        self.sift_up(len(self._values) - 1)

    def pop(self) -> typing.Any:
        first = self._values[0]
        pop_value = self._values.pop()

        if len(self._values) >= 1:
            self._values[0] = pop_value
            self.sift_down(0)

        return first

    def _get_children(self, idx: int) -> dict:
        children = {}
        left_idx = idx * 2 + 1
        if left_idx < len(self._values):
            children[self._values[left_idx]] = left_idx

        right_idx = left_idx + 1
        if right_idx < len(self._values):
            children[self._values[right_idx]] = right_idx

        return children

    def sift_down(self, idx: int) -> int:
        children = self._get_children(idx)
        if not children:
            return idx

        min_child = min(children)
        if min_child >= self._values[idx]:
            return idx

        min_child_idx = children[min_child]
        self._values[idx], self._values[min_child_idx] = self._values[min_child_idx], self._values[idx]
        return self.sift_down(min_child_idx)

    def sift_up(self, idx: int) -> int:
        if idx == 0:
            return idx

        parent_idx = (idx - 1) // 2
        if self._values[idx] >= self._values[parent_idx]:
            return idx

        self._values[idx], self._values[parent_idx] = self._values[parent_idx], self._values[idx]
        return self.sift_up(parent_idx)


def main() -> None:
    number = int(sys.stdin.readline())
    heap = Heap()

    for _ in range(number):
        username, tasks, fine = sys.stdin.readline().split()
        heap.add((-int(tasks), int(fine), username))

    for _ in range(number):
        result = heap.pop()
        print(result[2])


if __name__ == '__main__':
    main()

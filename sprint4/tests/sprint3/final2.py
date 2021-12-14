"""ID успешной посылки: 54599855

-- ПРИНЦИП РАБОТЫ --
Эффективная in-place быстрая сортировка. Быстрая сортировка без дополнительных массивов с результатами распределений.
Используются два указателя [left_pointer, right_pointer] с началом и концом отрезка, которые мы сдвигаем к центру, если
элементы находятся правильно относительно опорного элемента. Если элементы по указателям находятся неправильно
относительно нашего опорного элемента, то мы просто меняем их местами.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Работает аналогично обычной быстрой сортировки за O(n * log(n)). В худшем случае O(n ** 2).

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Пространственная сложность алгоритма равно O(log(n)) т.к. мы реализовали эффективную in-place быструю сортировку.
Мы не тратим место на хранение дополнительных массивов, но мы тратимся на дополнительные рекурсивные вызовы. В худшем
случае сложность будет равна O(n).
"""

import sys
import random
from typing import Any


def quick_sort(values: list[Any], left_pointer: int, right_pointer: int) -> None:
    if right_pointer - left_pointer == 0:
        return

    start, end = left_pointer, right_pointer
    pivot = random.choice(values[left_pointer:right_pointer + 1])
    while left_pointer < right_pointer:
        left_value, right_value = values[left_pointer], values[right_pointer]
        if left_value >= pivot >= right_value:
            values[left_pointer], values[right_pointer] = right_value, left_value

        left_pointer += left_value <= pivot
        right_pointer -= pivot <= right_value

    quick_sort(values, start, right_pointer)
    quick_sort(values, left_pointer, end)


def main() -> None:
    sys.stdin.readline()

    players = []
    for player in sys.stdin:
        try:
            name, score, fine = player.split()
            players.append((-int(score), int(fine), name))
        except ValueError:
            # В контесте в конце каждого теста выводится еще почему-то название теста.
            # Обрабатываю этот случай здесь.
            pass

    quick_sort(players, 0, len(players) - 1)
    for player in players:
        print(player[2])


if __name__ == '__main__':
    main()

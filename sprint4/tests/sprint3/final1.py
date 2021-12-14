"""ID успешной посылки: 54619606

-- ПРИНЦИП РАБОТЫ --
Бинарный поиск по сломанному массиву. Работает аналогично обычному двоичному поиску, но при неправильных границах
используются дополнительный проверки для того, чтобы определить в какой части массива находится элемент. Для удобства
я поместил рекурсивный вызов функции с поиском по частям в отдельные функции.

-- ВРЕМЕННАЯ СЛОЖНОСТЬ --
Работает аналогично бинарному поиску за O(log(n)). Каждую итерацию мы уменьшаем размер рассматриваемого массива вдвое.
Правда в данном случае делаем несколько лишний элементарных операций.

-- ПРОСТРАНСТВЕННАЯ СОЛЖНОСТЬ --
Пространственная сложность алгоритма равна O(log(n)).
"""


def binary_search(nums: list[int], target: int, left: int, right: int) -> int:
    if left == right:
        return -1

    middle = (left + right) // 2
    if nums[middle] == target:
        return middle

    def left_search() -> int:
        return binary_search(nums, target, left, middle)

    def right_search() -> int:
        return binary_search(nums, target, middle + 1, right)

    if nums[left] <= target < nums[middle]:
        return left_search()

    if nums[middle] < target <= nums[right - 1]:
        return right_search()

    if target < nums[middle] <= nums[right - 1]:
        return left_search()

    if nums[left] <= nums[middle] < target:
        return right_search()

    if nums[left] <= target:
        return left_search()

    return right_search()


def broken_search(nums: list, target: int) -> int:
    return binary_search(nums, target, 0, len(nums))

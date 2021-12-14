def merge(array: list, start_index: int, middle_index: int, end_index: int) -> list:
    left_pointer = start_index
    right_pointer = middle_index
    result = []

    while (left_pointer < middle_index) and (right_pointer < end_index):
        left_value, right_value = array[left_pointer], array[right_pointer]
        if left_value < right_value:
            result.append(left_value)
            left_pointer += 1
        else:
            result.append(right_value)
            right_pointer += 1

    left_remainder = array[left_pointer:middle_index]
    if left_remainder:
        result.extend(left_remainder)

    right_remainder = array[right_pointer:end_index]
    if right_remainder:
        result.extend(right_remainder)

    return result


def merge_sort(array: list, left: int, right: int) -> None:
    if right - left == 1:
        return

    middle = (left + right) // 2
    merge_sort(array, left, middle)
    merge_sort(array, middle, right)
    array[left:right] = merge(array, left, middle, right)

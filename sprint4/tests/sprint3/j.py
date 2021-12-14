def sort_by_bubble(values: list[int]) -> list[list[int]]:
    last_step = None
    length = len(values)
    for _ in range(length - 1):
        for curr_idx in range(1, length):
            prev_idx = curr_idx - 1
            if values[prev_idx] > values[curr_idx]:
                values[prev_idx], values[curr_idx] = values[curr_idx], values[prev_idx]

        if values == last_step:
            return

        print(*values)
        last_step = values.copy()


def main() -> None:
    input()
    unsorted = list(map(int, input().split()))
    sort_by_bubble(unsorted)


if __name__ == '__main__':
    main()

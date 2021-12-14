def search(values: tuple[int], search_value: int, left: int, right: int) -> int:
    if values[right] < search_value:
        return -1

    if left == right:
        return left + 1  # Прибавляем единицу к индексу тк нумерации при проверки начинается с 1

    middle = (left + right) // 2
    if values[middle] >= search_value:
        return search(values, search_value, left, middle)

    return search(values, search_value, middle + 1, right)


def main() -> None:
    input()
    savings = tuple(map(int, input().split()))
    cost = int(input())
    one_bike = search(savings, cost, 0, len(savings) - 1)
    two_bicycles = search(savings, cost * 2, 0, len(savings) - 1)
    print(one_bike, two_bicycles)
    

if __name__ == '__main__':
    main()

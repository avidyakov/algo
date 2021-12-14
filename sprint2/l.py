# 1 1 2 3 5 8 13 21 34 ...
def get_number_of_commits(number: int, k: int) -> int:
    """
    >>> get_number_of_commits(3, 1)
    3
    >>> get_number_of_commits(10, 1)
    9
    >>> get_number_of_commits(0, 1)
    1
    """
    num1, num2 = 1, 1
    for _ in range(number - 1):
        total = (num1 + num2) % 10 ** k
        num1, num2 = num2, total

    return num2


def main() -> None:
    n, k = map(int, input().split())
    print(get_number_of_commits(n, k))


if __name__ == '__main__':
    main()

# 1 1 2 3 5 8 13 21 34 ...
def get_number_of_commits(number: int) -> int:
    """
    >>> get_number_of_commits(0)
    1
    >>> get_number_of_commits(4)
    5
    """
    if number in {0, 1}:
        return 1

    return get_number_of_commits(number - 2) + get_number_of_commits(number - 1)


def main():
    number = int(input())
    print(get_number_of_commits(number))


if __name__ == '__main__':
    main()

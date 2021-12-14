def get_number_of_satisfied(children: list, cookies: list) -> int:
    """
    >>> get_number_of_satisfied([1, 2], [2, 1, 3])
    2
    >>> get_number_of_satisfied([2, 1, 3], [1, 1])
    1
    >>> get_number_of_satisfied([4], [1, 4, 7, 10, 2, 2, 7, 8])
    1
    """
    children.sort()
    cookies.sort()

    score = 0
    children_pointer = 0
    cookie_pointer = 0

    while (children_pointer < len(children)) and (cookie_pointer < len(cookies)):
        child, cookie = children[children_pointer], cookies[cookie_pointer]
        if child <= cookie:
            score += 1
            children_pointer += 1

        cookie_pointer += 1

    return score


def main() -> None:
    input()
    children = list(map(int, input().split()))
    input()
    cookies = list(map(int, input().split()))
    print(get_number_of_satisfied(children, cookies))


if __name__ == '__main__':
    main()

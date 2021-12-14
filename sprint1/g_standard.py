def factorize_number(number: int) -> list:
    """
    >>> factorize_number(8)
    [2, 2, 2]
    >>> factorize_number(100)
    [2, 2, 5, 5]
    """
    factors = []
    div = 2

    while div ** 2 <= number:
        quotient, remainder = divmod(number, div)
        if remainder:
            div += 1
            continue

        number = quotient
        factors.append(div)

    if number > 1:
        factors.append(number)

    return factors


def main() -> None:
    number = int(input())
    print(*factorize_number(number))


if __name__ == '__main__':
    main()

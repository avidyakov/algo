from math import sqrt


def eratosthenes_effective(n):
    """
    >>> eratosthenes_effective(10)
    [2, 3, 5, 7]
    >>> eratosthenes_effective(19)
    [2, 3, 5, 7, 11, 13, 17, 19]
    """
    numbers = list(range(n + 1))
    numbers[0] = numbers[1] = False
    for num in range(2, n):
        if numbers[num]:
            for j in range(num * num, n + 1, num):
                numbers[j] = False

    return [number for number in numbers if number]


def factorize_number(number: int) -> list:
    """
    >>> factorize_number(8)
    [2, 2, 2]
    >>> factorize_number(100)
    [2, 2, 5, 5]
    """
    factors = []
    prime_numbers = eratosthenes_effective(int(sqrt(number)))

    while number != 1:
        for factor in prime_numbers:
            quotient, remainder = divmod(number, factor)
            if not remainder:
                factors.append(factor)
                number = quotient
                break

    return factors


def main() -> None:
    number = int(input())
    print(*factorize_number(number))


if __name__ == '__main__':
    main()

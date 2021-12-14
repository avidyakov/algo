from itertools import zip_longest


def binary_sum(num1: str, num2: str) -> str:
    result = ''
    remains = 0
    for digits in zip_longest(num1[::-1], num2[::-1], fillvalue='0'):
        amount = sum(map(int, digits), remains)
        if amount < 2:
            result += str(amount)
            remains = 0
        else:
            result += str(amount - 2)
            remains = 1

    if remains:
        result += str(remains)

    return result[::-1]


def main() -> None:
    number1 = input()
    number2 = input()
    print(binary_sum(number1, number2))


if __name__ == '__main__':
    main()

def is_even(number: int) -> int:
    return number % 2 == 0


def are_all_of_the_same_parity(numbers) -> bool:
    parity_of_numbers = map(is_even, numbers)
    return sum(parity_of_numbers) in {0, 3}


if __name__ == '__main__':
    numbers = map(int, input().split())
    win = are_all_of_the_same_parity(numbers)
    print('WIN' if win else 'FAIL')

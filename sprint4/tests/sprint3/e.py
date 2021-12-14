def get_number_of_houses(prices: list, budget: int) -> int:
    """
    >>> get_number_of_houses([999, 999, 999], 300)
    0
    >>> get_number_of_houses([350, 999, 200], 1000)
    2
    """
    prices.sort()
    score = 0

    for price in prices:
        if budget < price:
            break

        budget -= price
        score += 1

    return score


def main() -> None:
    _, budget = input().split()
    prices = list(map(int, input().split()))
    print(get_number_of_houses(prices, int(budget)))


if __name__ == '__main__':
    main()

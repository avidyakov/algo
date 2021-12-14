def effective_solution(amount, numbers):
    """
    >>> effective_solution([])
    """
    history = set()
    n = len(numbers)
    triples = set()
    for i in range(n):
        for j in range(i + 1, n):
            target = amount - numbers[i] - numbers[j]
            if target in history:
                triples.add((target, numbers[i], numbers[j]))
        history.add(numbers[i])
    return triples


def main() -> None:
    input()
    amount = int(input())
    numbers = (int(i) for i in input().split())
    effective_solution(amount, numbers)


if __name__ == '__main__':
    main()

def get_randomness(temperatures):
    randomness = 0
    for index, temp in enumerate(temperatures):
        comparisons = []

        prev_index = index - 1
        if prev_index >= 0:
            comparisons.append(temperatures[prev_index] < temp)

        next_index = index + 1
        if next_index < len(temperatures):
            comparisons.append(temperatures[next_index] < temp)

        randomness += all(comparisons)

    return randomness


def maim():
    input()
    temperatures = map(int, input().split())
    print(get_randomness(temperatures))


if __name__ == '__main__':
    main()

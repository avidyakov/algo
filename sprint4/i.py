def get_the_longest_segment(team1, team2) -> int:
    """
    >>> get_the_longest_segment([1, 2, 3, 4], [1, 1, 2, 1, 2, 3, 3, 4])
    3
    >>> get_the_longest_segment([1, 2, 3, 2, 1], [3, 2, 1, 5, 6])
    3
    >>> get_the_longest_segment([1, 2, 3, 4, 5], [4, 5, 9])
    2
    """
    acc = {}
    for index, score in enumerate(team2):
        acc.setdefault(score, set()).add(index)

    lens = []

    prev = set()

    for score in team1:
        result = 0

        if score in acc:
            result = 1

            if prev := {i + 1 for i in prev} & acc[score]:
                result = lens[-1] + 1
            else:
                prev = acc[score]

        lens.append(result)

    return max(lens)


def main() -> None:
    input()
    team1 = map(int, input().split())
    input()
    team2 = map(int, input().split())
    print(get_the_longest_segment(team1, team2))


if __name__ == '__main__':
    main()

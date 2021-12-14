from collections import Counter


def get_anagrams(lines):
    acc = {}
    for index in range(len(lines)):
        acc.setdefault(frozenset(Counter(lines[index]).most_common()), []).append(index)

    return acc


def main() -> None:
    input()
    lines = input().split()
    for occurrences in get_anagrams(lines).values():
        print(*occurrences)


if __name__ == '__main__':
    main()

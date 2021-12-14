from functools import reduce


def get_polynomial_hash(a, m, string) -> int:
    """
    >>> get_polynomial_hash(123, 100003, 'a')
    97
    >>> get_polynomial_hash(123, 100003, 'hash')
    6080
    >>> get_polynomial_hash(123, 100003, 'HaSH')
    56156
    """
    if not string:
        return 0

    return reduce(lambda i1, i2: (i1 * a + ord(i2)) % m, string[1:], ord(string[0]))


def get_substring_hash(old_hash, first_letter, last_letter, a, m, string_len):
    """
    >>> get_substring_hash(79624, 'a', 'a', 123, 100_003, 3)
    94874
    """
    return ((old_hash - ord(first_letter) * a ** (string_len - 1)) * a + ord(last_letter)) % m


def get_substrings(string, substring_len, substring_occurrences, a=10**9+7, m=2**64):
    """
    >>> tuple(get_substrings('gggggooooogggggoooooogggggssshaa', 10, 2))
    (0, 5)
    >>> tuple(get_substrings('allallallallalla', 3, 4))
    (0, 1, 2)
    """
    acc = {}
    substring_hash = get_polynomial_hash(a, m, string[:substring_len])
    acc[substring_hash] = [0, 1]

    for end in range(substring_len, len(string)):
        start = end - substring_len
        substring_hash = get_substring_hash(substring_hash, string[start], string[end], a, m, substring_len)
        score = acc.setdefault(substring_hash, [start + 1, 0])
        score[1] += 1

    return map(
        lambda i: i[0],
        filter(lambda i: i[1] >= substring_occurrences, acc.values())
    )


def main() -> None:
    n, k = map(int, input().split())
    string = input()
    print(*get_substrings(string, n, k))


if __name__ == '__main__':
    main()

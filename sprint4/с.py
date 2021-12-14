import typing
from functools import reduce
from itertools import chain
from sys import stdin


def get_polynomial_hash(a: int, m: int, string: str) -> int:
    if not string:
        return 0

    return reduce(lambda i1, i2: (i1 * a + ord(i2)) % m, string[1:], ord(string[0]))


def get_substring_polynomial_hashes(
        a: int,
        m: int,
        string: str,
        gaps: typing.Generator[list, None, None]
) -> typing.Generator[int, None, None]:
    string_hash = get_polynomial_hash(a, m, string)
    string_len = len(string)

    for start, end in gaps:
        missing_idx = chain(range(0, start - 1), range(end, string_len))
        yield reduce(
            lambda i1, i2: i1 - ord(string[i2]) * a ** (string_len - i2 - 1),
            missing_idx,
            string_hash
        ) % m


def main() -> None:
    a, m = int(stdin.readline()), int(stdin.readline())
    string = stdin.readline().rstrip()
    stdin.readline()
    gaps = ([int(i) for i in line.split()] for line in stdin)

    for hash_ in get_substring_polynomial_hashes(a, m, string, gaps):
        print(hash_)


if __name__ == '__main__':
    main()

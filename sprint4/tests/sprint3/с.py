def is_subsequence(s: str, t: str) -> bool:
    """
    >>> is_subsequence('abc', 'ahbgdcu')
    True
    >>> is_subsequence('abcp', 'ahpc')
    False
    """
    if not s:
        return True

    acc = 0

    for letter in t:
        if letter == s[acc]:
            acc += 1

            if acc == len(s):
                return True

    return False


def main() -> None:
    s = input()
    t = input()
    print(is_subsequence(s, t))


if __name__ == '__main__':
    main()

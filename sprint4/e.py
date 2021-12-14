def get_length_of_substring(string: str) -> int:
    """
    >>> get_length_of_substring('abcabcbb')
    3
    >>> get_length_of_substring('bbbbb')
    1
    >>> get_length_of_substring('awe')
    3
    >>> get_length_of_substring('lu')
    2
    """
    string_len = len(string) + 1
    for n in range(string_len, 0, -1):
        for end in range(n, string_len):
            substring = string[end - n:end]
            if len(set(substring)) == len(substring):
                return n


def main() -> None:
    string = input()
    print(get_length_of_substring(string))


if __name__ == '__main__':
    main()

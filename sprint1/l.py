def get_extra_letter(string1: str, string2: str) -> str:
    """Получить лишнюю букву из второй строки.

    >>> get_extra_letter('abcd', 'abcde')
    'e'
    >>> get_extra_letter('go', 'ogg')
    'g'
    """
    for letter in string1:
        string2 = string2.replace(letter, '', 1)

    return string2


def main() -> None:
    string1 = input()
    string2 = input()
    print(get_extra_letter(string1, string2))


if __name__ == '__main__':
    main()

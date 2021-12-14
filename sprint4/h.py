def strange_equality(string1, string2) -> bool:
    """
    >>> strange_equality('mxyskaoghi', 'qodfrgmslc')
    True
    >>> strange_equality('agg', 'xdd')
    True
    >>> strange_equality('agg', 'xda')
    False
    >>> strange_equality('aba', 'xxx')
    False
    >>> strange_equality('abacaba', 'abacabac')
    False
    """
    if len(string1) != len(string2):
        return False

    matches = {}
    for letter1, letter2 in zip(string1, string2):
        match = matches.get(letter1)
        if match is None:
            if letter2 in matches.values():
                return False

            matches[letter1] = letter2
            continue

        if match != letter2:
            return False

    return True


def main() -> None:
    string1 = input()
    string2 = input()
    result = strange_equality(string1, string2)
    print('YES' if result else 'NO')


if __name__ == '__main__':
    main()

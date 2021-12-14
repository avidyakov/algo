LETTERS = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz'
}


def get_letter_combinations(keys: str, combination: str = '') -> None:
    if len(keys) == 0:
        print(combination, end=' ')
        return

    first_key, *other_keys = keys
    for letter_of_key in LETTERS[first_key]:
        get_letter_combinations(other_keys, combination + letter_of_key)


def main() -> None:
    keys = input()
    get_letter_combinations(keys)
    print()


if __name__ == '__main__':
    main()

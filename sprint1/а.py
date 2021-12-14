def is_palindrome(sentence):
    empty_string = ''
    formatted = sentence.strip().replace(
        ' ', empty_string
    ).replace(
        '.', empty_string
    ).replace(
        ',', empty_string
    ).replace(
        ':', empty_string
    ).lower()

    return formatted == ''.join(reversed(formatted))


def main():
    sentence = input()
    print(is_palindrome(sentence))


if __name__ == '__main__':
    main()

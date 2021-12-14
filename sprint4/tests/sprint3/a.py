def gen_binary(length, max_length, sequence: str = '') -> None:
    if length == 0:
        print(sequence)
        return

    open_brackets = sequence.count('(')
    close_brackets = sequence.count(')')

    if open_brackets < max_length:
        gen_binary(length - 1, max_length, sequence + '(')

    if (close_brackets < max_length) and (open_brackets > close_brackets):
        gen_binary(length - 1, max_length, sequence + ')')


def main() -> None:
    length = int(input())
    gen_binary(length * 2, length)


if __name__ == '__main__':
    main()

BRACKETS = {
    '(': ')',
    '[': ']',
    '{': '}',
}


def is_correct_bracket_seq(bracket_seq: str) -> bool:
    """
    >>> is_correct_bracket_seq('{[()]}')
    True
    >>> is_correct_bracket_seq('()')
    True
    >>> is_correct_bracket_seq('(()')
    False
    >>> is_correct_bracket_seq('())')
    False
    """
    stack = []

    for bracket in bracket_seq:
        if bracket in BRACKETS.keys():
            stack.append(bracket)
        elif stack and BRACKETS[stack[-1]] == bracket:
            stack.pop()
        else:
            return False

    return not stack


def main():
    line = input()
    print(is_correct_bracket_seq(line))


if __name__ == '__main__':
    main()

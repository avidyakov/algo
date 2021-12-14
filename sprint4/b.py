import random
import string

from a import get_polynomial_hash

A = 1000
M = 123_987_123
N = 20


def main() -> None:
    while True:
        string1 = ''.join(random.choices(string.ascii_lowercase, k=N))
        string2 = ''.join(random.choices(string.ascii_lowercase, k=N))

        if get_polynomial_hash(A, M, string1) == get_polynomial_hash(A, M, string2):
            print(string1, string2)
            break


if __name__ == '__main__':
    main()

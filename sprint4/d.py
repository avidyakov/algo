import sys


def main():
    sys.stdin.readline()
    groups = {line.rstrip(): 0 for line in sys.stdin}
    for group in groups:
        print(group)


if __name__ == '__main__':
    main()

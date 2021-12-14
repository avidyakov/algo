def main():
    input()
    number1 = int(input().replace(' ', ''))
    number2 = int(input())
    print(*(tuple(str(number1 + number2))))


if __name__ == '__main__':
    main()

class Stack:

    def __init__(self):
        self._values = []

    def pop(self) -> int:
        return self._values.pop()

    def push(self, value: int) -> None:
        self._values.append(value)

    def get_max(self) -> int:
        if self._values:
            return max(self._values)


def main():
    number_of_commands = int(input())
    stack = Stack()

    for _ in range(number_of_commands):
        row = input()
        if 'get_max' in row:
            print(stack.get_max())
        elif 'push' in row:
            value = int(row.split()[-1])
            stack.push(value)
        else:
            try:
                stack.pop()
            except IndexError:
                print('error')


if __name__ == '__main__':
    main()

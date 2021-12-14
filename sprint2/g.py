import sys


class Stack:

    def __init__(self):
        self._values = []
        self._max_values = []

    def pop(self) -> int:
        pop_value = self._values.pop()
        if pop_value == self._max_values[-1]:
            self._max_values.pop()

        return pop_value

    def push(self, value: int) -> None:
        self._values.append(value)
        if not self._max_values or value >= self._max_values[-1]:
            self._max_values.append(value)

    def get_max(self) -> int:
        if self._values:
            return self._max_values[-1]


def main():
    number_of_commands = int(sys.stdin.readline().rstrip())
    stack = Stack()
    result = []

    for _ in range(number_of_commands):
        line = sys.stdin.readline().rstrip()
        if 'get_max' in line:
            result.append(stack.get_max())
        elif 'push' in line:
            value = int(line.split()[-1])
            stack.push(value)
        else:
            try:
                stack.pop()
            except IndexError:
                result.append('error')

    print(*result, sep='\n')


if __name__ == '__main__':
    main()

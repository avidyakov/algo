import sys


class AllowedNumberOfElements(Exception):
    pass


class LimitedQueue:

    def __init__(self, max_size: int):
        self._max_size = max_size
        self._values = [None] * self._max_size
        self._head = self._tail = self._size = 0

    def peek(self):
        return self._values[self._head]

    def push(self, value: int):
        if self._size < self._max_size:
            self._values[self._tail] = value
            self._tail = (self._tail + 1) % self._max_size
            self._size += 1
        else:
            raise AllowedNumberOfElements

    def size(self):
        return self._size

    def pop(self):
        if self._size:
            pop_value = self._values[self._head]
            self._values[self._head] = None
            self._head = (self._head + 1) % self._max_size
            self._size -= 1
            return pop_value


def main() -> None:
    number_of_commands = int(sys.stdin.readline().rstrip())
    queue_size = int(sys.stdin.readline().rstrip())
    queue = LimitedQueue(queue_size)

    for _ in range(number_of_commands):
        line = sys.stdin.readline().rstrip()
        if 'peek' in line:
            print(queue.peek())
        elif 'push' in line:
            _, value = line.split()
            try:
                queue.push(int(value))
            except AllowedNumberOfElements:
                print('error')
        elif 'size' in line:
            print(queue.size())
        else:
            print(queue.pop())


if __name__ == '__main__':
    main()

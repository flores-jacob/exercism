from collections import deque


class BufferFullException(Exception):
    def __init__(self):
        Exception.__init__(self, "Buffer is full")


class BufferEmptyException(Exception):
    def __init__(self):
        Exception.__init__(self, "Buffer is empty")


class CircularBuffer(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = deque(maxlen=capacity)

    def read(self):
        try:
            return self.buffer.pop()
        except IndexError:
            raise BufferEmptyException

    def write(self, data):
        if len(self.buffer) < self.capacity:
            self.buffer.appendleft(data)
        else:
            raise BufferFullException

    def clear(self):
        self.buffer.clear()

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException:
            self.buffer.appendleft(data)
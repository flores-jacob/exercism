from collections import deque

class BufferFullException(Exception):
    def __init__(self):
        Exception.__init__(self, "Buffer is full")


class BufferEmptyException(Exception):
    def __init__(self):
        Exception.__init__(self, "Buffer is empty")


class CircularBuffer(object):
    def __init__(self, capacity):
        self.buffer = [None] * capacity
        # self.op_queue = deque([0], 5)
        self.read_index = 0
        self.write_index = 0
        self.capacity = capacity

    def read(self):
        if self.buffer[self.read_index] is None:
            raise BufferEmptyException

        data_val = self.buffer[self.read_index]
        self.buffer[self.read_index] = None

        print("data_one", self.read_index)

        self.read_index += 1
        # If we have reached the end of the buffer, reset count to 0
        if self.read_index == self.capacity:
            self.read_index = 0

        print("data_two", self.read_index)

        return data_val

    def write(self, data):
        if all(x is not None for x in self.buffer):
            raise BufferFullException

        self.buffer[self.write_index] = data

        # Move to the next index
        self.write_index += 1

        # If we have reached the end of the buffer, reset count to 0
        if self.write_index == self.capacity:
            self.write_index = 0



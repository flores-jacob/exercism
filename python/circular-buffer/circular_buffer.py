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
        self.write_queue = deque([], capacity)
        self.capacity = capacity

    def read(self):
        if self.buffer[self.read_index] is None:
            raise BufferEmptyException

        # Assign data and remove after reading
        data_val = self.buffer[self.read_index]
        self.buffer[self.read_index] = None

        # Move to the next index
        self.read_index = (self.read_index + 1) % self.capacity

        return data_val

    def write(self, data):
        if all(x is not None for x in self.buffer):
            raise BufferFullException

        self.write_queue.append(self.write_index)
        self.buffer[self.write_index] = data

        # Move to the next index
        self.write_index = (self.write_index + 1) % self.capacity

    def clear(self):
        self.buffer = [None] * self.capacity

    def overwrite(self, data):
        try:
            self.write(data)
        except BufferFullException:
            oldest_index = self.write_queue.popleft()
            self.buffer[oldest_index] = data
            self.write_queue.append(oldest_index)

            # Move to the next index
            self.write_index = (oldest_index + 1) % self.capacity
            self.read_index = (oldest_index + 1) % self.capacity

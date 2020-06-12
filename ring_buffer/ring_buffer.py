
from collections import deque
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        for x in range(capacity):
            self.data.append(None)
        self.current=0

    def append(self, item):
        if self.current == self.capacity:
            self.current = 0
        self.data[self.current] = item
        self.current += 1

    def get(self):
        #filter out None values we used to initialize list to max, capacity. Trim list down if we only appended #items < capacity
        data = []
        for x in self.data:
            if x != None:
                data.append(x)
        return data
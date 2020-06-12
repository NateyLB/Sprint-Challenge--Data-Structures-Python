
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.data = []
        for x in range(capacity):
            self.data.append(x)
        self.current=0

    def append(self, item):
        if self.current == self.capacity:
            self.current = 0
        self.data[self.current] = item
        self.current += 1
        print(self.current)

    def get(self):
        return self.data
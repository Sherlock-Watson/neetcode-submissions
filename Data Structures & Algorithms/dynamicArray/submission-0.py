class DynamicArray:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.length = 0
        self.array = [0] * capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.length >= self.capacity:
            self.resize()
        self.array[self.length] = n
        self.length += 1

    def popback(self) -> int:
        tmp = self.array[self.length - 1]
        self.array[self.length - 1] = 0
        self.length -= 1
        return tmp

    def resize(self) -> None:
        self.capacity *= 2
        array = [0] * self.capacity
        for i in range(0, self.length):
            array[i] = self.array[i]
        self.array = array

    def getSize(self) -> int:
        return self.length

    def getCapacity(self) -> int:
        return self.capacity

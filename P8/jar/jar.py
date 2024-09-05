class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity
        self.size = 0

    def __str__(self):
        return self._size *"🍪"

    def deposit(self, n):
        if (n>(self._capacity-self._size)):
            raise ValueError
        self.size += n

    def withdraw(self, n):
        if n > self._size:
            raise ValueError
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self,capacity):
        if capacity<0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self,size):
        if size > self._capacity:
            raise ValueError
        self._size = size


class MyCircularQueue(object):
    def __init__(self, k):
        self.__start = 0
        self.__size = 0
        self.__buffer = [0] * k

    def enQueue(self, value):
        if self.isFull():
            return False
        self.__buffer[(self.__start+self.__size) % len(self.__buffer)] = value
        self.__size += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.__start = (self.__start+1) % len(self.__buffer)
        self.__size -= 1
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.__buffer[self.__start]

    def Rear(self):
        return -1 if self.isEmpty() else self.__buffer[(self.__start+self.__size-1) % len(self.__buffer)]

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == len(self.__buffer)
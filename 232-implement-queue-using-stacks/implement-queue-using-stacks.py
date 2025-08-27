class ArrayStack:
    def __init__(self, size=1000):
        self.top = -1
        self.size = size
        self.arr = [0] * self.size

    def push(self, x):
        if self.top == self.size - 1:
            raise OverflowError("Stack is full")
        self.top += 1
        self.arr[self.top] = x

    def pop(self):
        if self.top == -1:
            raise IndexError("Pop from empty stack")
        x = self.arr[self.top]
        self.top -= 1
        return x

    def peek(self):  # renamed from top() -> peek() (common convention)
        if self.isEmpty():
            raise IndexError("Peek from empty stack")
        return self.arr[self.top]

    def isEmpty(self):
        return self.top == -1


class MyQueue:

    def __init__(self):
        self.s = ArrayStack()
        self.s2 = ArrayStack()

    def push(self, x: int) -> None:
        if self.s.isEmpty():
            self.s.push(x)
        else:
            while not self.s.isEmpty():
                self.s2.push(self.s.pop())
            self.s.push(x)
            while not self.s2.isEmpty():
                self.s.push(self.s2.pop())


    def pop(self) -> int:
        return self.s.pop()

    def peek(self) -> int:
        return self.s.peek()

    def empty(self) -> bool:
        return self.s.isEmpty()


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
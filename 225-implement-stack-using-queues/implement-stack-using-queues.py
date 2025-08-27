class Queue:

    def __init__(self):
        self.arr = [0]*1000
        self.start = -1
        self.end = -1
        self.currsize = 0
    def push(self,x):
        if self.isEmpty():
            self.start = 0
            self.end = 0
        else:
            self.end +=1
        self.arr[self.end] = x
        self.currsize +=1 
        
    def pop(self):
        if not self.isEmpty():
            x = self.arr[self.start]
            self.start+=1
            self.currsize -=1
            return x
        else:
            print("isEmpty")

    def peek(self):
        return self.arr[self.start] if not self.isEmpty() else None

    def size(self):
        return self.currsize

    def isEmpty(self):
        return self.currsize == 0


class MyStack:

    def __init__(self):
        self.q = Queue() 

    def push(self, x: int) -> None:
        if self.q.size() == 0:
            self.q.push(x)
        else:
            n = self.q.size()
            self.q.push(x)
            for i in range(n):
                y = self.q.pop()
                self.q.push(y)
            
            
             

    def pop(self) -> int:
        return self.q.pop()

    def top(self) -> int:
        return self.q.peek()

    def empty(self) -> bool:
        return self.q.isEmpty()


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
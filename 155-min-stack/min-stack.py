class MinStack:

    def __init__(self):
        self.Top = -1
        self.size = 3 * 10**4
        self.arr = [[0,0]]*self.size
        self.min = float('inf')

    def push(self, val: int) -> None:
        self.Top+=1
        if val < self.min:
            self.min = val
        self.arr[self.Top] = [val,self.min]
        

    def pop(self) -> None:
        self.Top-=1
   
        self.min = self.arr[self.Top][1]
        if self.Top == -1:
            self.min = float('inf')

    def top(self) -> int:
        return self.arr[self.Top][0]

    def getMin(self) -> int:  
        return self.min
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
class Stack:
    def __init__(self):
        self.Top = -1
        self.size = 10**4+1
        self.arr = [0]*self.size

    def push(self, x):
        self.Top+=1
        print(self.Top,self.size)
        self.arr[self.Top] = x
        

    def pop(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        x = self.arr[self.Top]
        self.Top-=1
        return x

    def top(self):
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.arr[self.Top]
     

    def isEmpty(self):
        return self.Top == -1
            

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        c = [")" , "]", "}"]
        o = ["(", "[","{"]
        se = dict(zip(c,o))
        for i in s:
            if i in o:
                stack.push(i)

            elif stack.isEmpty():
                return False
                break
            
            elif i in c:
            
                if se[i] == stack.top():
                    stack.pop()
                else:
                    return False
                    break

        if stack.isEmpty():
            return True
        else:
            return False
class Stack:
    def __init__(self):
        self.Top = -1
        self.size = 10**4
        self.arr = [0]*self.size

    def push(self, x):
        self.Top+=1
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
        stack = []
        c = [")" , "]", "}"]
        o = ["(", "[","{"]
        se = dict(zip(c,o))
        for i in s:
            if i in o:
                # stack.push(i)
                stack.append(i)

            
            elif i in c:
                if stack == []:
                    return False

                # if se[i] == stack.top():
                if se[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                    
        # if stack.isEmpty():
        return not stack
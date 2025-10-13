class Stack:
    def __init__(self):
        self.Top = -1
        self.size = 10**4
        self.arr = [0]*self.size

    def push(self, x):
        self.Top+=1
        self.arr[self.Top] = x
        
    def pop(self) -> str:
        if self.isEmpty():
            raise IndexError("Stack is empty")
        x = self.arr[self.Top]
        self.Top-=1
        return x

    def top(self) -> str:
        if self.isEmpty():
            raise IndexError("Stack is empty")
        return self.arr[self.Top]

    def isEmpty(self):
        return self.Top == -1

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        st = Stack()
        n = len(nums)
        nge = [-1]*n
        # ind = nums.index(max(nums))
        # print(ind)
        for i in range(2*n-1,-1,-1):
            i = i%n
            while not st.isEmpty() and st.top() <= nums[i]:
                st.pop()
            print(st.isEmpty())
            if not st.isEmpty():
                nge[i] = st.top()
                # print(st.top())
            st.push(nums[i])
            # print(nge)

        return nge


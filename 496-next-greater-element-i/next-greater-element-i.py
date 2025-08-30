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
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st = Stack()
        n = len(nums2)
        nge = [-1]*n
        for i in range(n-1,-1,-1):
            while not st.isEmpty() and st.top() < nums2[i]:
                st.pop()
            if not st.isEmpty():
                nge[i] = st.top()
            st.push(nums2[i])

        ans = []
        for i in nums1:
            ans.append(nge[nums2.index(i)])
        return ans
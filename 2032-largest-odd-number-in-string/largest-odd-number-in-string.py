class Solution:
    def largestOddNumber(self, num: str) -> str:
        ans = ""
        for i in range(len(num)-1, -1,-1):
            d = int(num[i])
            if d%2 != 0:
                ans = num[:i+1]
                break
                
                
        return ans


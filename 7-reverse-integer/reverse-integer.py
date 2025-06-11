class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        if x < 0:
            x = -x
            neg = True
        b = 0
        while x !=0:
            b = (b*10) + (x%10)
            x = x//10
        if neg:
           b = -b
        if b > -(2**31) and b < ((2**31) - 1):
            return b
        return 0
        
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # if n&(n-1) == 0 and n!=0:
        #     return True
        # return False
        if n<= 0:
            return False
        if bin(n).count('1') == 1:
            return True
        return False
            
class Solution:
    def myPow(self, x: float, n: int) -> float:
        ans = 1
        nn = n
        if nn < 0:
            nn = nn*-1
        
        while nn:
            if nn %2 :
                ans*= x
                nn -= 1
            else:
                x*=x
                nn //= 2
        
        return ans if n>=0 else 1/ans


        return ans
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # ans = 1
        # nn = n
        # if nn < 0:
        #     nn = nn*-1
        
        # while nn:
        #     if nn %2 :
        #         ans*= x
        #         nn -= 1
        #     else:
        #         x*=x
        #         nn //= 2
        
        # return ans if n>=0 else 1/ans

        
        if n == 0: return 1
        if n<0:
            n = n*-1
            return 1/self.myPow(x,n)
        res = self.myPow(x , n//2)
        if n%2 == 0:
            return res*res
        else:
            return x*res*res
        
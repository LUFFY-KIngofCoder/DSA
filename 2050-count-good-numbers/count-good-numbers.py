MOD = 10**9 + 7 
def pow(x,n):
    if n == 0: return 1
    res = pow(x,n//2)
    if n%2:
        return (x * res * res)%MOD
    else:
        return (res * res)%MOD


class Solution:
    def countGoodNumbers(self, n: int) -> int:
        Even  = [0,2,4,6,8]
        prime = [2,3,5,7]

        o_place = n//2  
        e_place = o_place if n%2 == 0 else (n - o_place) 
       
        ans =  (pow(len(prime),o_place) * pow(len(Even),e_place)) % MOD

        return ans
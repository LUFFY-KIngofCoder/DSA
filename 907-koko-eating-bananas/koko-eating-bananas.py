from math import ceil
def yn(nums,k):
    ans = 0
    for i in nums:
        ans += ceil(i/k)
    return ans

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
            
        l = 1
        r = max(piles)
        mid = 0
        while l<r:
            mid = (l+r)//2
            
            if yn(piles,mid) <= h : 
                r= mid

            else:
                l = mid+1
       
        return l
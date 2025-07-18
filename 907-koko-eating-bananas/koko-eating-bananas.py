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
        ans = float('inf')
        while l<=r:
            mid = (l+r)//2
            print(mid,yn(piles,mid) , l, r)
            if yn(piles,mid) <= h :
                print(mid)
                ans = min(ans,mid)
                r= mid-1
            elif yn(piles,mid) > h :
                l = mid+1
            
        return ans
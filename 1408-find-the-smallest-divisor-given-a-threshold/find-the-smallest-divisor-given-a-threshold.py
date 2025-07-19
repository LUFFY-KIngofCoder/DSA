import math
def isthreshold(nums,k,threshold): 
    return sum(math.ceil(i/k) for i in nums) <= threshold
     

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:    
        l = 1
        r = max(nums)
        while l<=r:
            mid = (l+r)//2
            if isthreshold(nums,mid,threshold):
                r = mid-1
            else:
                l = mid+1
        return l
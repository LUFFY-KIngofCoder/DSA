def ispossible(nums,total):
    cnt = 1
    s = 0
    for i in nums:
        s+=i
        if s > total:
            cnt+=1
            s=i
        
    return cnt

class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        l = min(nums)
        r = sum(nums)

        while l<=r:
            mid = (l+r)//2
            print(mid,l,r)
            if ispossible(nums,mid) > k:
                l=mid+1
            else:
                r=mid-1
        ans = 0
        s = 0
        for i in nums:
            s+=i
            if s > l:
                ans = max(ans, s-i)
                s=i

        ans = max(ans, s)
        return ans



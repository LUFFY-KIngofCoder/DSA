def no_bouque(nums, d,k):
    count = 0
    c=0
    for i in nums:
        if i - d <= 0:
            c+=1
        else: 
            c=0
        if c == k:
            count+=1
            c=0

    return count


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if len(bloomDay) < m*k:
            return -1
        
        l= min(bloomDay)
        r = max(bloomDay)
        flow = m*k

        while l<r:
            mid = (l+r)//2
            print(l , r, mid, no_bouque(bloomDay , mid,k))
            if no_bouque(bloomDay , mid,k) >= m:
                r = mid
            else:
                l=mid+1

        return l

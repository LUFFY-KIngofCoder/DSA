def no_bouque(nums,d,k): # better
    cnt = 0
    c = 0
    for i in nums:
        if i <= d:
            c +=1
        else:
            cnt+= c//k
            c = 0
    cnt+= c//k
    return cnt


def no_bouque1(nums, d,k): #okay
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
            print(l , r, mid, no_bouque1(bloomDay , mid,k))
            if no_bouque(bloomDay , mid,k) >= m:
                r = mid
            else:
                l=mid+1

        return l
#--------------------------------------------
        # val = m * k
        # n = len(bloomDay)  # size of the array
        # if val > n:
        #     return -1  # impossible case
        # # find maximum and minimum
        # mini = float('inf')
        # maxi = float('-inf')
        # for i in range(n):
        #     mini = min(mini, bloomDay[i])
        #     maxi = max(maxi, bloomDay[i])

        # # apply binary search
        # low = mini
        # high = maxi
        # while low <= high:
        #     mid = (low + high) // 2
        #     if possible(bloomDay, mid, m, k):
        #         high = mid - 1
        #     else:
        #         low = mid + 1
        # return low
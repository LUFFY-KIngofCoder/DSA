# def result(nums, m, days):
#     s = 0
#     d = 0
#     for i in range(len(nums)):
#         s += nums[i]
#         if s == m:
#             d+=1
#             s=0
#         elif s > m:
#             d+=1
#             s=nums[i]
         
#     d += 1 if s != 0 else 0 
#     print(d)
#     return d <= days

def result(nums, m, days):
    s = 0
    d = 1
    for i in range(len(nums)):
        if s + nums[i] > m:
            d+=1
            s=nums[i]
        else:
            s+=nums[i]
         
    print(d)
    return d <= days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        r = sum(weights)
        if days == 1:
            return r

        l = max(weights)

        while l<=r:
            mid = (l+r)//2    
            print(mid,l,r)
            if result(weights,mid,days):
                r=mid-1
            else:
                l=mid+1
            
        
        return l
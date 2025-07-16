class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        # ans = nums[0]
        # mid=((l+r)//2)
        # while l<r:
        #     # ans = nums[mid]
        #     # print(ans,l,r)
        #     # if l == r:
        #     #     break
        #     if nums[l] > nums[mid]:
        #         r = mid
        #     else:
        #         if nums[l] > nums[r]:
        #             l = mid+1
        #         else:
        #             mid = l
        #             break
        #     mid=((l+r)//2)
        # return nums[mid]
#-------------------------------------------
        ans = nums[0]
        while l<=r:
            mid = (l+r)//2
            if nums[l] > nums[mid]:
                r = mid-1
                ans = min(ans , nums[mid])

            else:
                ans = min(ans,nums[l])
                l= mid+1
                
        return ans
        

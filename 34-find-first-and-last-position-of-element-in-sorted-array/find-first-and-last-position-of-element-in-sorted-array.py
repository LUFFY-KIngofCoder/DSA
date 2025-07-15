class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        n=len(nums)
        # l=0
        # r=n-1
        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid] == target:
        #         ans[1] = mid
        #         l = mid+1 
        #     elif nums[mid] > target:
        #         r= mid-1
        #     else:
        #         l= mid+1

        # l=0
        # r=n-1
        # while l<=r:
        #     mid = (l+r)//2
        #     if nums[mid] == target:
        #         ans[0] = mid
        #         r = mid-1
        #     elif nums[mid] > target:
        #         r= mid-1
        #     else:
        #         l= mid+1
#------------------------------------------------------
        l=0
        r=n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                l = mid
                r = mid
                while l>=0 and nums[l] == target:
                    l-=1
                while r<len(nums) and nums[r] == target:
                    r+=1
                ans = [l+1,r-1]
                break
            elif nums[mid] > target:
                r= mid-1
            else:
                l= mid+1


        return ans
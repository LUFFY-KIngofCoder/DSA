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
                while l-1>=0 and nums[l-1] == target:
                    l-=1
                while r+1<len(nums) and nums[r+1] == target:
                    r+=1
                ans = [l,r]
                break
            elif nums[mid] > target:
                r= mid-1
            else:
                l= mid+1


        return ans
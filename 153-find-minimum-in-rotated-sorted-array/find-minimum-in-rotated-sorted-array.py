class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = nums[0]
        while l<=r:
            mid=((l+r)//2)
            ans = min(ans,nums[mid])
            if nums[l] > nums[mid]:
                r = mid-1
            else:
                if nums[l] > nums[r]:
                    l = mid+1
                else:
                    r = mid-1

        return ans

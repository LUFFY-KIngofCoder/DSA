class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        if 1 not in nums:
            return 0
        if 0 not in nums:
            return len(nums)-1
        
        ans = 0
        prev = 0
        curr = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                curr += 1
            if nums[i] == 0 or i == len(nums)-1:
                ans = max(ans , prev+curr)
                prev = curr
                curr = 0
            i+=1
        return ans


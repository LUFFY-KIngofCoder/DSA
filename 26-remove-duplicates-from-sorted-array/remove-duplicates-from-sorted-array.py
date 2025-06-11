class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        p = 1
        for i in range(n):
            if nums[i] != nums[p-1]:
                nums[p] , nums[i] = nums[i],nums[p]
                p+=1
            
        return p
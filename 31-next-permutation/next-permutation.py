class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = None
        n = len(nums)
        for i in range(n-1):
            if nums[i+1] > nums[i]:
                a = i
        
        if a == None:
            nums.sort()
            return

        m = None
        for i in range(a+1,n):
            if (m == None) and (nums[i] > nums[a]):
                m = i
            elif nums[i] > nums[a] and nums[i] < nums[m]:
                    m = i
        
        nums[m] , nums[a] = nums[a] , nums[m]
        nums[a+1:] = sorted(nums[a+1:])
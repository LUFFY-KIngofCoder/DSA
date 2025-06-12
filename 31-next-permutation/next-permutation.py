class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = None
        n = len(nums)
        for i in range(n-1,0,-1):
            if nums[i] > nums[i-1]:
                a = i-1
                break
        
        if a == None:
            nums.sort()
            return

        #m = None
        # for i in range(a+1,n):
        #     if (m == None) and (nums[i] > nums[a]):
        #         m = i
        #     elif nums[i] > nums[a] and nums[i] < nums[m]:
        #             m = i
        # nums[m] , nums[a] = nums[a] , nums[m]

        for j in range(n-1, a,-1):
            if nums[j] > nums[a]:
                nums[j] , nums[a] = nums[a] , nums[j]
                break

        nums[a+1:] = nums[:a:-1]
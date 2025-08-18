# def answer(nums , ds,ans):
#     if len(nums) == len(ds):
        


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # ds = []
        n = 1 << len(nums)

        ans= []
        for i in range(n):
            s = []
            for j in range(len(nums)):
                if (i & 1 << j):
                    s.append(nums[j])
            ans.append(s)
        
        return ans
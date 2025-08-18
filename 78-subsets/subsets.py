def answer(nums , ds,ans, i):
    if i == len(nums):
        ans.append(ds.copy())
        return
    
    ds.append(nums[i])
    answer(nums,ds,ans,i+1)
    ds.pop()    
    answer(nums,ds,ans,i+1)

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # n = 1 << len(nums)

        # ans= []
        # for i in range(n):
        #     s = []
        #     for j in range(len(nums)):
        #         if (i & 1 << j):
        #             s.append(nums[j])
        #     ans.append(s)
        
        # return ans

#---------------------------------
        ds = []
        ans = []
        answer(nums,ds,ans,0)
        return ans
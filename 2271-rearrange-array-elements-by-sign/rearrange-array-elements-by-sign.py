class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        # p = 0
        # n = 1
        # new = nums.copy()
        # for i in range(len(nums)):
        #     if nums[i] >= 0 :
        #         new[p] = nums[i] 
        #         p+=2
        #     else:
        #         new[n] = nums[i]
        #         n+=2
        # return new

        p = [i for i in nums if i >=0]
        n = [i for i in nums if i < 0]
        new = []
        for i in range(len(p)):
            new.append(p[i])
            new.append(n[i])

        return new
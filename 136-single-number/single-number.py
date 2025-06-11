class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # a = {}
        # for i in nums:
        #     if i not in a:
        #         a[i] = 1
        #     else:
        #         a[i] += 1

        # return list(a.keys())[list(a.values()).index(1)]

        res = 0
        for i in nums:
            res = i ^ res
        return res
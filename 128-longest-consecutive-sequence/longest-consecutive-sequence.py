class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        maxi = 0
        for i in s:
            count = 0
            if i-1 not in s:
                j = i
                while j in s:
                    count+=1
                    j+=1
            maxi = max(count,maxi)
        return maxi
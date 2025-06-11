class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxi = 0
        a = 0
        for i in nums:
            if i == 0:
                maxi = max(a,maxi)
                a = 0
                
            else:
                a += 1

        return max(maxi,a)
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        h = {}
        n = len(nums)
        m = n/3
        ans = []

        for i in nums:
            if i in h:
                h[i] +=1
            else:
                h[i] = 1
    
        for i in h:
            if h[i] > m:
                ans.append(i)

        return ans
    
                
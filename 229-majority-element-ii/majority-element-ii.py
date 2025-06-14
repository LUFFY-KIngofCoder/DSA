class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # h = {}
        # n = len(nums)
        # m = n/3
        # ans = []

        # for i in nums:
        #     if i in h:
        #         h[i] +=1
        #     else:
        #         h[i] = 1
    
        # for i in h:
        #     if h[i] > m:
        #         ans.append(i)

        nums.sort()
        i = 0
        j = 0
        n = len(nums)
        ans = []
        while(j < n):
            if nums[i] != nums[j]:
                if j-i > n/3:
                    ans.append(nums[i])
                i = j
            j+=1
        if j-i > n/3:
            ans.append(nums[i])

        return ans
    
                
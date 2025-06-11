class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            res = target - nums[i]
            if res in a:
                return [a[res] , i]
            else:
                a[nums[i]] = i
        

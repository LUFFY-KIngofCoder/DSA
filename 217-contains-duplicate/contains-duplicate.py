class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        l = nums
        s = set(l)
        if len(s) != len(l):
            return True
        else:
            return False
        
        
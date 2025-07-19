class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        l = 0
        c = 0
        while c < k:
            l+=1
            if l not in arr:
                c+=1
            
        return l
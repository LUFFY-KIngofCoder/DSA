class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        for i in arr:
            if i > k :
                break
            k+=1
        return k
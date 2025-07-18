from collections import defaultdict

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count=0
        MOD = 10**9+7
        right = defaultdict(int)
        for num in nums:
            right[num]+=1
        
        left = defaultdict(int)

        for num in nums:
            
            right[num]-=1
            
            val = num*2

            count += (right[val]%MOD) * (left[val]%MOD)
            count %=MOD

            left[num]+=1
        
        return count


        return count 

            
from collections import defaultdict,Counter

class Solution:
    def specialTriplets(self, nums: List[int]) -> int:
        count=0
        MOD = 10**9+7
        right = Counter(nums)
        
        left = defaultdict(int)

        for num in nums:
            
            right[num]-=1
            
            val = num*2

            count += (right[val]%MOD) * (left[val]%MOD)
            count %=MOD

            left[num]+=1
        
        return count


        return count 

            
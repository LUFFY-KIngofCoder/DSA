from collections import Counter
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            for j in range(i+1,n):
                count = Counter(s[i:j+1])
                mini = min(count.values())
                maxi = max(count.values())
                if mini!= maxi and mini != 0:
                    ans+= maxi-mini
        return ans
        
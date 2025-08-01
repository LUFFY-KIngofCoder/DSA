from collections import Counter, defaultdict
class Solution:
    def beautySum(self, s: str) -> int:
        n = len(s)
        ans = 0
        for i in range(n):
            m = defaultdict(int)
            # for j in range(i+1,n):
                # count = Counter(s[i:j+1])
                # mini = min(count.values())
                # maxi = max(count.values())
                # if mini!= maxi and mini != 0:
                #     ans+= maxi-mini/
            for j in range(i,n):
                m[s[j]]+=1
                ans += max(m.values()) - min(m.values())
        return ans
        
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # has = {}
        # s = 0
        # n = 0

        # for i in nums:
           
        #     s += i

        #     if s == k:
        #         n+=1
            
        #     res = s - k

        #     if res in has:
        #         n+= has[res]

        #     if s not in has:
        #         has[s] = 1
        #     else:
        #         has[s] +=1

        # return n

        h = defaultdict(int)
        s = 0
        h[0] = 1
        cnt = 0
        for i in nums:
            s += i
            cnt += h[s - k]
            h[s] +=1
        return cnt




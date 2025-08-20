class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        ds = []

        def answer(i):
            if i == len(s):
                ans.append(ds.copy())
                return
            for j in range(i,len(s)):
                if s[i:j+1] == s[i:j+1][::-1]:
                    ds.append(s[i:j+1])
                    answer(j+1)
                    ds.pop()
                

        answer(0)
        return ans
                

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        max_l = max([len(i) for i in wordDict])
        wordDict = set(wordDict)
        memo = {}

        def answer(p):
            if p == n:
                return True
            if p in memo:
                return memo[p]
            # print(p)
            for i in range(p,n):
                if i-p+1 > max_l:
                    break
                
                word = s[p:i+1]
                if word in wordDict and answer(i+1):
                    memo[p] = True
                    return True
            memo[p] = False
            return False
        
        return answer(0)
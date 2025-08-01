class Solution:
    def isPal(self, s):
            return s == s[::-1]
    def longestPalindrome(self, s: str) -> str:
        # if s == s[::-1]:
        #     return s
        # n=len(s)
        # f = {}
        # ans = s[0]
        # for i in range(n): 
        #     if s[i] in f.keys():
        #         for j in f[s[i]]:  
        #             r = s[j:i+1]
        #             if r == r[::-1] and len(r) > len(ans):
        #                 ans = r
        #         f[s[i]].append(i)
        #     else:
        #         f[s[i]] = [i]
            
        # return ans

        

        ans = ""
        for i in range(len(s)):
            for j in range(i, len(s)):
                if self.isPal(s[i:j+1]):
                    if len(ans) < len(s[i:j+1]):
                        ans = s[i:j+1]
        return ans
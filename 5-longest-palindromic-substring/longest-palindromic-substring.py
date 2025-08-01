class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        f = {}
        ans = s[0]
        for i in range(n):
           
            if s[i] in f.keys():
                for j in f[s[i]]:  
                    r = s[j:i+1]
                    p = s[i:j-1:-1] if j!= 0 else s[i::-1]
                   
                    if r == p and len(r) > len(ans):
                        ans = r
                f[s[i]].append(i)
            else:
                f[s[i]] = [i]
            
        return ans
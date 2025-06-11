class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        high = 0
        i = 0
        j = 0
        a = []
        while j < len(s) and i < len(s):
            if s[j] not in a:
                a.append(s[j])
                high  = max(high , j-i+1)
                j+=1
                
            else:
                i += 1
                j = i
                a = []

        return high
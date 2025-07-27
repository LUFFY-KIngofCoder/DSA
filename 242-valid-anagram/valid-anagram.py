class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return Counter(s) == Counter(t)
#--------------------------------------------------------
        n = len(s)
        m = len(t)
        if n != m:
            return False
        # a = {}
        # b = {}
        # for i in range(n):
        #     if s[i] not in a:
        #         a[s[i]] = 1
        #     else:
        #         a[s[i]] +=1 
            
        #     if t[i] not in b:
        #         b[t[i]] = 1
        #     else:
        #         b[t[i]] +=1
        # for i in a:
        #     if (i not in b) or (a[i] != b[i]):
        #         return False
        # return True
#--------------------------------------------------------
        ss = set(s)
        for i in s:
            if s.count(i) != t.count(i):
                return False
        return True
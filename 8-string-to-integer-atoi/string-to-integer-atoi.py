class Solution:
    def myAtoi(self, s: str) -> int:
        if s == '':
            return 0
        while len(s)>1 and s[0] == ' ':
            s = s[1:]
        ans = '0'
        isneg = -1 if s[0] == '-' else 1
        s = s[1:] if s[0] in ["-", '+'] else s
        for i in s:
            if i.isdigit():
                ans = ans+i
            else:
                break
        ans = isneg*int(ans)
        lb = -2**31
        ub = 2**31 - 1
        if ans < lb:
            return lb
        elif ans > ub:
            return ub
        else:
            return ans
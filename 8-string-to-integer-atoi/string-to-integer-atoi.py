def atoi(s):

    def remove_starting(s):
        if s == "" or s[0] != " "  :
            return s
        return remove_starting(s[1:])
    s = remove_starting(s)
    if s == "":
        return 0
    sign = -1 if s[0] == "-" else 1
    if s[0] in ["-", "+"]:
        s= s[1:]

    def get_number(s, i):
        if i >= len(s) or s[i].isdigit() == False :
            return s[:i]
        return get_number(s,i+1)
    s = get_number(s,0)
    if s == "":
        return 0
    return sign*int(s)


class Solution:
    def myAtoi(self, s: str) -> int:
        # s = s.strip()
        # if s == '':
        #     return 0
        # # while len(s)>1 and s[0] == ' ':
        # #     s = s[1:] 
        
        # ans = '0'
        # isneg = -1 if s[0] == '-' else 1
        # s = s[1:] if s[0] in ["-", '+'] else s
        # for i in s:
        #     if i.isdigit():
        #         ans = ans+i
        #     else:
        #         break
        # ans = isneg*int(ans)
        # lb = -2**31
        # ub = 2**31 - 1
        # if ans < lb:
        #     return lb
        # elif ans > ub:
        #     return ub
        # else:
        #     return ans

        ans = atoi(s)

        if ans < -2**31:
            return -2**31
        elif ans > 2**31 - 1:
            return 2**31 - 1
        return ans
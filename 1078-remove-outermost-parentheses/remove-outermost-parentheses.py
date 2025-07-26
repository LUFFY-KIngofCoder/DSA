class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        new = ""
        cnt = 0
        for i in s:
            if i == "(":
                cnt+=1
                if cnt > 1:
                    new = new + i
            elif i== ")":
                cnt-=1
                if cnt > 0:
                    new = new + i

        return new
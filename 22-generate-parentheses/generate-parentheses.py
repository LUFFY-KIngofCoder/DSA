def answer(s , ans, n,count):
    if len(s)== n*2:
        ans.append(s)
        return 
    if s.count("(")!= n:    
        answer(s+"(" , ans, n, count+1)
    if s != "" and count != 0:
        answer(s+")" , ans, n, count-1)

    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ""
        ans = []
        answer(s,ans,n,0)
        return ans
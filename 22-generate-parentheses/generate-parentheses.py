def answer(s , ans, n,f,b):
    if len(s)== n*2:
        ans.append(s)
        return 
    if f!= n:    
        answer(s+"(" , ans, n, f+1,b)
    if f!= 0 and f!= b :
        answer(s+")" , ans, n, f,b+1)

    
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        s = ""
        ans = []
        answer(s,ans,n,0,0)
        return ans
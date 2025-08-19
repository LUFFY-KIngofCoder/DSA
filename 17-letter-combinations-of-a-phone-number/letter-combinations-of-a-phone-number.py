class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits== "":
            return []
        
        alpha = ["","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]

        ans = []
        
        def answer(i , s):
            if i == len(digits):
                ans.append(s)
                return
            for j in alpha[int(digits[i])-1]:
                print(int(digits[i]),j)
                answer(i+1,s+j)
        
        answer(0,"")
        return ans


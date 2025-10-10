class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []      

        def answer(start=0,s = "",lo = 0,t = 0):

            if start == len(num):
                if t == target:
                    ans.append(s)
                return
            
            for i in range(start,len(num)):
                if i > start and num[start] == "0":
                    return
                
                curr = int(num[start:i+1])


                if start == 0:
                    answer(i+1,f"{curr}",curr,t = curr)
                else:
                    answer(i+1,f"{s}*{curr}",lo = lo*curr, t = t-lo+lo*curr)
                    answer(i+1,f"{s}-{curr}",lo = -curr, t = t-curr)
                    answer(i+1,f"{s}+{curr}",lo = curr, t = t+curr)
                    
                    
                    
        answer()
        return ans
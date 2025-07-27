class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False
        # n= len(s)
        # start = goal[0]
        # k = 0
        # while k < n:
        #     try:    
        #         k = s.index(start,k)
        #         if s[k:]+s[:k] == goal:
        #             return True
        #         k+=1
        #     except:
        #         break
        # return False 
        
        if goal in s+s:
            return True
        else:
            return False
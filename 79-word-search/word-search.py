class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        def answer(i , j ,s):  
            if s == word:
                return True

            temp, board[i][j] = board[i][j], "#"

            if i!=0 and word[len(s)] == board[i-1][j]: 
                top = answer(i-1,j,s+board[i-1][j])
                if top:
                    return True
            
            
            if j!= len(board[0])-1 and word[len(s)] == board[i][j+1]:
                right = answer(i,j+1,s+board[i][j+1])
                if right:
                    return True
        
            
            if j!= 0 and word[len(s)] == board[i][j-1]:
                left = answer(i,j-1,s+board[i][j-1])
                if left:
                    return True
            
            
            if i!= len(board)-1 and word[len(s)] == board[i+1][j]:
                bottom = answer(i+1,j,s+board[i+1][j])
                if bottom:
                    return True
            board[i][j] = temp
            return False
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    ans = answer(i,j,word[0])
                    if ans:
                        return True
        return False
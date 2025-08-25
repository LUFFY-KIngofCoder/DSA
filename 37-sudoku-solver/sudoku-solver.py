
class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        row = {i: set() for i in range(9)}
        col = {i: set() for i in range(9)}
        box = {(i, j): set() for i in range(3) for j in range(3)}
        empty = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    row[i].add(board[i][j])
                    col[j].add(board[i][j])
                    box[(i//3,j//3)].add(board[i][j])
                else:
                    empty.append((i,j))


        # def check(row,col,n):
        #     for i in range(9):
        
        #         if board[i][col] == n:
        #             return False
        #         if board[row][i] == n:
        #             return False
        #         if board[3 * (row//3) + (i//3)][3 * (col//3) + (i%3)] == n:
        #             return False
        #     return True


        # def solver():
        #     for i in range(9):
        #         for j in range(9):
        #             if board[i][j]==".":    
        #                 for k in range(1,10):
        #                     if str(k) not in row[i] and str(k) not in col[j] and str(k) not in box[(i//3,j//3)]:
                                
        #                         board[i][j]=str(k)
        #                         row[i].add(board[i][j])
        #                         col[j].add(board[i][j])
        #                         box[(i//3,j//3)].add(board[i][j])
        #                         if solver():
        #                             return True
        #                         row[i].remove(board[i][j])
        #                         col[j].remove(board[i][j])
        #                         box[(i//3,j//3)].remove(board[i][j])
        #                         board[i][j] = "."
        #                 return False


        def solver(l):
                if l == len(empty):
                    return True 

                i,j = empty[l]
                for k in range(1,10):
                    if str(k) not in row[i] and str(k) not in col[j] and str(k) not in box[(i//3,j//3)]:
                        
                        board[i][j]=str(k)
                        row[i].add(board[i][j])
                        col[j].add(board[i][j])
                        box[(i//3,j//3)].add(board[i][j])
                        if solver(l+1):
                            return True
                        row[i].remove(board[i][j])
                        col[j].remove(board[i][j])
                        box[(i//3,j//3)].remove(board[i][j])
                        board[i][j] = "."
                return False
                    
        solver(0) 
            

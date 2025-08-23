class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        # def check(i,j,ds):
            
        #     #top right
        #     a= i-1
        #     b = j-1
        #     while a>=0 and b>=0:
        #         if ds[a][b] == "Q":
        #             return False
        #         a-=1
        #         b-=1
        #     #top left
        #     a= i-1
        #     b = j+1
        #     while a>=0 and b<n:
        #         if ds[a][b] == "Q":
        #             return False
        #         a-=1
        #         b+=1
        #     return True

        # def answer(row,ds,hist_col):
        #     if row == n:
        #         ans.append(ds)
        #         return
        #     for col in range(n):
        #         if col not in hist_col:
        #             if check(row,col,ds):
        #                 s = "."*(col) +"Q" + "."*(n-col-1)
        #                 answer(row+1 , ds+[s],hist_col+[col])
                
        # answer(0,[],[])
        # return ans

#---------------------------------------------------------
        board = [["."]*n for _ in range(n)]

        col = set()
        rdiag = set()
        ldiag = set()

        def answer(i):
            if i == n:
                a = ["".join(row) for row in board]
                ans.append(a)
                return
            
            for j in range(n):
                if j in col or (i-j) in rdiag or (i+j) in ldiag:
                    continue
                
                col.add(j)
                rdiag.add(i-j)
                ldiag.add(i+j)

                board[i][j] = "Q"

                answer(i+1)

                board[i][j] = "."

                col.remove(j)
                rdiag.remove(i-j)
                ldiag.remove(i+j)
        answer(0)
        return ans
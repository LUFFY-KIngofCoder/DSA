class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []

        def check(i,j,ds):
            
            #top right
            a= i-1
            b = j-1
            while a>=0 and b>=0:
                if ds[a][b] == "Q":
                    return False
                a-=1
                b-=1
            #top left
            a= i-1
            b = j+1
            while a>=0 and b<n:
                if ds[a][b] == "Q":
                    return False
                a-=1
                b+=1
            return True

        def answer(row,ds,hist_col):
            if row == n:
                ans.append(ds)
                return
            for col in range(n):
                if col not in hist_col:
                    if check(row,col,ds):
                        s = "."*(col) +"Q" + "."*(n-col-1)
                        answer(row+1 , ds+[s],hist_col+[col])
                
        answer(0,[],[])
        return ans
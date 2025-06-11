class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        x = set() 
        y = set()

        for i in range(m):
            if 0 in matrix[i]:
                x.add(i)
                for j in range(n):
                    if 0 == matrix[i][j]:
                        y.add(j)
        for i in x:
            for j in range(n):
                matrix[i][j] = 0
        
        for j in y:
            for i in range(m):
                matrix[i][j] = 0
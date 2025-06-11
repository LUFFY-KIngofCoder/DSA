class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        m = len(matrix[0])
        x = []
        y = set()

        for i in range(n):
            if 0 in matrix[i]:
                # start = 0
                x.append(i)
                # while True:
                #     try:
                #         yi = matrix[i].index(0 , start)
                #         start = yi+1
                #         y.add(yi)
                        
                #     except:
                #         break  
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        y.add(j)


        for j in x:
            for i in range(m):
                matrix[j][i] = 0
        
        for j in y:
            for i in range(n):
                matrix[i][j] = 0
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        # for i in range(n): #T.C. = O(n*log(m))
        #     l = 0
        #     r = m-1
        #     while l<=r:
        #         mid = (l+r)//2
        #         if matrix[i][mid] > target:
        #             r = mid -1
        #         elif matrix[i][mid] < target:
        #             l = mid+1
        #         else:
        #             return True
        # return False
#-------------------------------------------------
        row = 0
        col = m-1

        while row < n and col > -1:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row+=1
            else:
                col-=1
        return False
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            l = 0
            r = m-1
            while l<=r:
                mid = (l+r)//2
                if matrix[i][mid] > target:
                    r = mid -1
                elif matrix[i][mid] < target:
                    l = mid+1
                else:
                    return True
        return False
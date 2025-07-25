class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
    #     l = 0
    #     r = n-1
    #     print(m,n)
    #     while l<=r:
    #         mid = (l+r)//2
    #         if matrix[mid][0] > target:
    #             r = mid-1
    #         elif matrix[mid][0] < target:
    #             l = mid+1
    #         else:
    #             r = mid
    #             break
            
    #     i = r
    #     print(l,r) 

    #     l = 0 
    #     r = m-1

    #     while l<=r:
    #         mid = (l+r)//2
    #         if matrix[i][mid] > target:
    #             r = mid -1
    #         elif matrix[i][mid] < target:
    #             l=mid+1
    #         else:
    #             return True
#--------------------------------------------------
        l= 0
        r = m*n-1
        while l<=r:
            mid = (l+r)//2
            row = mid//m
            col = mid%m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                l=mid+1
            else:
                r = mid-1

        return False           
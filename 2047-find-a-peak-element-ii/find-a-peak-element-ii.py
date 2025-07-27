class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        n = len(mat)
        m = len(mat[0])
        r = 1
        col = m-2
        l = 0
        r = m-1
        i = 0
        while i < n: 
            print('a->',[i,l,r])
            while l<=r:
                mid = (l+r)//2
                print('b->',[i,l,r])
                if mid!=m-1 and mat[i][mid] < mat[i][mid+1]:
                    if l!=r:
                        l=mid+1
                    else:
                        r = mid+1
                elif mid!= 0 and mat[i][mid] < mat[i][mid-1]:
                    if l!=r:
                        r=mid-1
                    else:
                        l=mid-1
                elif i!= n-1 and mat[i][mid] < mat[i+1][mid]:
                    i+=1
                    break
                elif i!= 0 and mat[i][mid] < mat[i-1][mid]:
                    i-=1
                    break
                else:
                    return [i,mid]
            
                
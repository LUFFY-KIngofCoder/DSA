def max_ele(mat ,mid, n):
    idx , mx = -1, -1
    for i in range(n):
        if mat[i][mid] > mx:
            mx = mat[i][mid]
            idx = i
    return idx
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
            
#------------------------------
        # l = 0
        # r = m - 1

        # while l <= r:
        #     mid = (l+r)//2
        #     print(l,r,mid)
        #     idx = max_ele(mat,mid,n)

        #     if mid < m-1 and mat[idx][mid+1] > mat[idx][mid]:
        #         l=mid+1
        #     elif mid > 0 and mat[idx][mid-1] > mat[idx][mid]:
        #         r=mid-1
        #     else:
        #         return [idx, mid]  
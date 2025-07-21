class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        
        # for i in arr:
        #     if i > k :
        #         break
        #     k+=1
        # return k

#-----------------------------------------------
        n = len(arr)
        l=0
        r = n-1
        while l<=r:
            mid= (l+r)//2
            if arr[mid] - mid -1 < k:
                l = mid +1
            else:
                r = mid-1
        if r == -1:
            return k

        ans =  k + r + 1         # arr[r] + (k - (arr[r]- r-1))
        return ans
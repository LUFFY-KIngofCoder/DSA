def swap(arr1 , arr2 ,left , right):
    if arr1[left] > arr2[right]:
        arr1[left] , arr2[right] = arr2[right] , arr1[left]


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # a = nums1[:m]
        # i = 0
        # j = 0
        # for k in range(m+n):
        #     if i >=m:
        #         nums1[k] = nums2[j]
        #         j+=1
        #     elif j>=n:
        #         nums1[k] = a[i]
        #         i+=1
        #     elif a[i] <= nums2[j]:
        #         nums1[k] = a[i]    
        #         i+=1
        #     elif a[i] > nums2[j]:
        #         nums1[k] = nums2[j]
        #         j+=1

#--------------------------------------------------------------------------------------------
        # while n > 0 :
        #     if nums1[m-1] >= nums2[n-1] and m >0:
        #         nums1[m+n-1] = nums1[m-1]
        #         m-=1
        #     else:
        #         nums1[m+n-1] = nums2[n-1]
        #         n-=1 
#--------------------------------------------------------------------------------------------

        #gap sort/ Shell Sort

        gap = ((m+n)//2)+((m+n)%2)

        while gap > 0:
            left = 0 
            right = left + gap
            
            while right < m+n:

                if left < m  and right >=m: 
                    swap(nums1,nums2, left,right-m)
                
                elif left >=m:
                    swap(nums2,nums2  ,left-m ,right-m)

                else:
                    swap(nums1, nums1,left ,right)
                
                left+=1
                right+=1

            if gap == 1:
                break

            gap = ((gap)//2)+((gap)%2)

 
        for i in range(n):
            nums1[m+i] = nums2[i]

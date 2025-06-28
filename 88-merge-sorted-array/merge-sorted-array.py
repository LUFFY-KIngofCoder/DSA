class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = nums1[:m]
        i = 0
        j = 0
        for k in range(m+n):
            if i >=m:
                nums1[k] = nums2[j]
                j+=1
            elif j>=n:
                nums1[k] = a[i]
                i+=1
            elif a[i] <= nums2[j]:
                nums1[k] = a[i]    
                i+=1
            elif a[i] > nums2[j]:
                nums1[k] = nums2[j]
                j+=1
            
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        new = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        while (i < m and j < n):
            if nums1[i] <= nums2[j]:
                new.append(nums1[i])
                i+=1
            else:
                new.append(nums2[j])
                j+=1
        while(i<m):
            new.append(nums1[i])
            i+=1
        while(j<n):
            new.append(nums2[j])
            j+=1

        l = m+n
        med = int(l/2)
        return new[med] if (l%2 != 0) else (new[med]+new[med-1])/2
        
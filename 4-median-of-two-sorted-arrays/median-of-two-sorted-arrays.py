class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # new = []
        # i = 0
        # j = 0
        # m = len(nums1)
        # n = len(nums2)
        # while (i < m and j < n):
        #     if nums1[i] <= nums2[j]:
        #         new.append(nums1[i])
        #         i+=1
        #     else:
        #         new.append(nums2[j])
        #         j+=1
        # while(i<m):
        #     new.append(nums1[i])
        #     i+=1
        # while(j<n):
        #     new.append(nums2[j])
        #     j+=1

        # l = m+n
        # med = int(l/2)
        # return new[med] if (l%2 != 0) else (new[med]+new[med-1])/2
#-----------------------------       
        m = len(nums1)
        n = len(nums2)
        
        ind2 = (m+n)//2
        ind1 = ind2-1
        
        ind1e = -1
        ind2e = -1
        cnt = -1
        print(ind1,ind2)
        i = 0
        j = 0
        while i < m and j < n :
            cnt+=1
            if nums1[i]<= nums2[j]:
                if cnt == ind1:
                    ind1e = nums1[i]
                elif cnt== ind2:
                    ind2e = nums1[i]
                    break
                i+=1
                
            else:
                if cnt == ind1:
                    ind1e = nums2[j]
                elif cnt== ind2:
                    ind2e = nums2[j]
                    break
                j+=1
            
        while(i<m):
            cnt+=1
            if cnt == ind1:
                ind1e = nums1[i]
            elif cnt== ind2:
                ind2e = nums1[i]
                break
            i+=1
        while(j<n):
            cnt+=1
            if cnt == ind1:
                ind1e = nums2[j]
            elif cnt== ind2:
                ind2e = nums2[j]
                break
            j+=1
        print(ind1,ind2)
        if (m+n)%2 == 0:
            return (ind1e+ind2e)/2
        else:
            return ind2e
            
            


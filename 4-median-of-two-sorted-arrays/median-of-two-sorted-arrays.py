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
        # m = len(nums1)
        # n = len(nums2)
        
        # ind2 = (m+n)//2
        # ind1 = ind2-1
        
        # ind1e = -1
        # ind2e = -1
        # cnt = -1
        # print(ind1,ind2)
        # i = 0
        # j = 0
        # while i < m and j < n :
        #     cnt+=1
        #     if nums1[i]<= nums2[j]:
        #         if cnt == ind1:
        #             ind1e = nums1[i]
        #         elif cnt== ind2:
        #             ind2e = nums1[i]
        #             break
        #         i+=1
                
        #     else:
        #         if cnt == ind1:
        #             ind1e = nums2[j]
        #         elif cnt== ind2:
        #             ind2e = nums2[j]
        #             break
        #         j+=1
            
        # while(i<m):
        #     cnt+=1
        #     if cnt == ind1:
        #         ind1e = nums1[i]
        #     elif cnt== ind2:
        #         ind2e = nums1[i]
        #         break
        #     i+=1
        # while(j<n):
        #     cnt+=1
        #     if cnt == ind1:
        #         ind1e = nums2[j]
        #     elif cnt== ind2:
        #         ind2e = nums2[j]
        #         break
        #     j+=1
        # print(ind1,ind2)
        # if (m+n)%2 == 0:
        #     return (ind1e+ind2e)/2
        # else:
        #     return ind2e
#-----------------------------   
        m = len(nums1)
        n = len(nums2)

        if n<m:
            m , n = n, m
            nums1, nums2 = nums2 , nums1

        if m == 0:
            if n%2 !=0:
                return nums2[n//2]
            else:
                mid = n//2
                return (nums2[mid]+nums2[mid-1])/2    
        
        l = 0
        r = m         
        split = (m+n)//2
        print(split)

        # while l<=r:
        #     mid = (l+r)//2
            
        #     if mid != 0 and mid != m:
        #         if nums1[mid-1] > nums2[split-mid]:
        #             r = mid-1
        #         else:
        #             l = mid+1
        #     elif mid == 0:
        #         if nums2[split-1] <= nums1[0]:
        #             l = mid+1
        #         else:
        #             r = mid+1
        #     elif mid == m:
        #         if nums1[-1] <= nums2[split-m]:
        #             l = mid+1
        #         else:
        #             r=mid - 1
        #     print(mid,l,r)
        # ans = r
        # print(ans)
        # if ans == m:
        #     le = nums1[-1]
        #     re = nums2[split-ans]
        # elif ans == 0:
        #     le = nums2[split-1]
        #     re = min(nums1[0] , nums2[split-ans])
        # else:
        #     le = max(nums1[ans-1] , nums2[split-ans-1])
        #     re = min(nums1[ans], nums2[split-ans])
        # print(ans ,le,re)
        # if (m+n)%2 == 0:
        #     return (le+re)/2
        # else:
        #     return re
            
        while l <= r:
            mid1 = (l+r)//2
            mid2 = split - mid1

            l1,l2,r1,r2 = float('-inf'),float('-inf'),float('inf'),float('inf')
            if mid1 <= m and mid1 != 0:
                l1 = nums1[mid1-1]
            if mid2 <= n and mid2 != 0:
                l2 = nums2[mid2 -1]
            if mid1 >=0 and mid1 != m:
                r1 = nums1[mid1]
            if mid2 >=0 and mid2 < n:
                r2 = nums2[mid2]

            if l1 <= r2 and l2 <= r1:
                if (n+m)%2 == 0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return min(r1,r2)
            
            elif l1 > r2:
                r = mid1-1
            elif l2 > r1:
                l = mid1+1
            
            


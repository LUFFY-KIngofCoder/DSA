from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
      
        ####T.C. = O(n)
        # h = {}
        # n = len(nums)
        # m = n/3
        # ans = []

        # for i in nums:
        #     if i in h:
        #         h[i] +=1
        #     else:
        #         h[i] = 1
        #     if h[i] > m and i not in ans:
        #         ans.append(i)

        # or 

        # h = Counter(nums)
    
        # for i in h:
        #     if h[i] > m:
        #         ans.append(i)
#---------------------------------------------------------------------------
        ####T.C. = O(n log n) 
        # nums.sort()
        # i = 0
        # j = 0
        # n = len(nums)
        # ans = []
        # while(j < n):
        #     if nums[i] != nums[j]:
        #         if j-i > n/3:
        #             ans.append(nums[i])
        #         i = j
        #     j+=1
        # if j-i > n/3:
        #     ans.append(nums[i])
#---------------------------------------------------
        e1 = 0
        e2 = 0
        cnt1 = 0
        cnt2 = 0
        
        n= len(nums)
        ans = []
        
        for i in nums:
            if cnt1 == 0 and i != e2:
                e1 = i
                cnt1 = 1
            elif cnt2 == 0 and i != e1:
                e2 = i
                cnt2 = 1
            elif i == e1:
                cnt1 +=1
            elif i == e2:
                cnt2 += 1
            else:
                cnt1 -= 1
                cnt2 -= 1

        cnt1 = 0
        cnt2 = 0

        for i in nums:
            if i == e1:
                cnt1 += 1
            elif i == e2:
                cnt2 += 1
        
        if cnt1 > n/3:
            ans.append(e1)
        if cnt2 > n/3: 
            ans.append(e2)


        return ans
    
                
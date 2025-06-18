class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ###T.C. = O(n^2 log(m))
        # n = len(nums)
        # ans = set()
        # for i in range(n):
        #     h =[]
             
        #     for j in range(i+1,n):
        #         if -(nums[i] + nums[j]) in h:
        #             a = [nums[i] ,-(nums[i] + nums[j]), nums[j]]
        #             print(a)
        #             t = tuple(sorted(a))
        #             ans.add(t)
                
        #         h.append(nums[j])
        
        ans = []
        nums.sort()
        n = len(nums)

        for i in range(n):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            j = i+1
            k = n-1
            while(j<k):
                total = nums[i]+nums[j]+nums[k]
                if total == 0 :
                    ans.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    
                    while nums[j] == nums[j-1] and j<k:
                        j+=1
                    while nums[k] == nums[k+1] and j <k:
                        k-=1
                elif total > 0:
                    k-=1
                else:
                    j+=1
            
        return ans


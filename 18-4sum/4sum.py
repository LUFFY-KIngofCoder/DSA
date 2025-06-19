class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        n = len(nums)

        for l in range(n-3):
            if l != 0 and nums[l] == nums[l - 1]:
                    continue
            for i in range(l+1,n-2):
                if nums[i] == nums[i - 1] and i!= l+1:
                    continue
                
                j = i+1
                k = n-1
                while(j<k):
                    total = nums[i]+nums[j]+nums[k]+nums[l]
                    if total == target :
                        ans.append([nums[l],nums[i],nums[j],nums[k]])
                        j += 1
                        k -= 1

                        while j<k and nums[j] == nums[j-1]  :
                            j+=1
                        while j<k and nums[k] == nums[k+1] :
                            k-=1
                    elif total > target:
                        k-=1
                    else:
                        j+=1
                
        return ans

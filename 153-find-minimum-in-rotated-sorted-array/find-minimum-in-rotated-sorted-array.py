class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        r = n-1
        ans = nums[0]
        mid=((l+r)//2)
        while l<r:
            # ans = nums[mid]
            # print(ans,l,r)
            # if l == r:
            #     break
            if nums[l] > nums[mid]:
                r = mid
            else:
                if nums[l] > nums[r]:
                    l = mid+1
                else:
                    r = mid
            mid=((l+r)//2)
            
        return nums[mid]

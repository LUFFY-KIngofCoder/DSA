class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        l = 0
        r = n-1

        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                return True
            if nums[l] > nums[mid]:
                if nums[r] >= target and nums[mid] <= target:
                    l = mid+1
                else:
                    r= mid-1
            elif nums[l] < nums[mid]:
                if nums[l] <= target and nums[mid] >= target:
                    r = mid-1
                else:
                    l= mid+1
            else:
                while l<=r and nums[l] == nums[mid] :
                    l+=1
                while l<=r and nums[r] == nums[mid]:
                    r-=1

        return False
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        m = min(nums)
        k = nums.index(m)
        if k!= 0:
            nums = nums[k:]+nums[:k]

        print(nums,k)
        n = len(nums) 
        low = 0
        high = n - 1

        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid+k if mid+k < n else mid+k-n
            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1
        return -1
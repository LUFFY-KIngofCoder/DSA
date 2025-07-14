class Solution:
    def search(self, nums: List[int], target: int) -> int:
        ans = -1
        n=len(nums)
        l=0
        r=n-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid] == target:
                ans = mid
                return ans
            elif nums[mid] > target:
                r= mid-1
            else:
                l= mid+1
            print(l,r)
        return ans
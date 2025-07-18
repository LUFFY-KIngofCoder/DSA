class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return 0

        l = 0
        r = n-1
        ans = 0

        while l<=r:
            mid = (l+r)//2
            if mid !=0 and mid!=n-1:
                if nums[mid] > nums[mid-1] and nums[mid] > nums[mid+1]:
                    ans = mid
                    break
                elif nums[mid] < nums[mid-1]:
                    r = mid-1
                elif nums[mid] < nums[mid+1]:
                    l = mid+1
                else:
                    t = mid+2
                    while nums[t] <= nums[mid] and t >=0:
                        t-=1
                    if t==-1:
                        t = mid+2
                        while nums[t] <= nums[mid] and t <n:
                            t+=1
                        l=t
                    else:
                        r = t

            elif mid ==0:
                if nums[mid] > nums[mid+1]:
                    ans = mid
                    break
                elif nums[mid] < nums[mid+1]:
                    l = mid+1
            elif mid ==n-1:
                if nums[mid] > nums[mid-1]:
                    ans = mid
                    break
                elif nums[mid] < nums[mid+1]:
                    r = mid-1
            
        return ans
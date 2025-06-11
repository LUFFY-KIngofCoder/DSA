class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # check = []
        n = len(nums)
        k = k%n
        # j = n-k

        # while(i < k):
        #     check.append(nums[i])
        #     nums[i] = nums[j]
        #     i+=1
        #     j+=1
        # j = 0
        # while(i < n):
        #     check.append(nums[i])
        #     nums[i] = check[j]
        #     i+=1
        #     j+=1

        nums[:] = nums[n-k:] + nums[:n-k]
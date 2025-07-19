
    

class Solution:
    def splitArray(self, nums: List[int]) -> int:

        if len(nums)<=2:
            return abs(sum(nums))


        n = len(nums)
        prime = [True] * n
        prime[0], prime[1] = False, False
        p = 2
        while p*p <= n:
            if prime[p] == True:
                for i in range(p*p , n,p):
                    prime[i] = False
            p+=1


        A = 0
        B = 0
        for i in range(len(nums)):
            if prime[i]:
                A+=nums[i]
            else:
                B+=nums[i]
        return abs(A - B)
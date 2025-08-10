def per(nums,ds,freq,ans):
    if len(nums) == len(ds):
        ans.append(ds.copy())
        return
    for i in range(len(nums)):
        if freq[i] == 0:
            ds.append(nums[i])
            freq[i] = 1
            per(nums,ds,freq,ans)
            freq[i] = 0
            ds.pop()
            
class Solution:
    def reorderedPowerOf2(self, n: int) -> bool:
        
        # nums = list(str(n))
        # freq = [0]*len(nums)
        # ds = []
        # ans = []
        # per(nums , ds,freq,ans)
        # # print(ans)
        # for i in ans:
        #     if i[0] != '0':
        #         number = int("".join(i))
        #         if number & (number-1) == 0:
        #             # print(i,number)
        #             return True
        # return False 

        def counter(x):
            return sorted(str(x))
        
        n_counter = counter(n)
        for i in range(31): #10**9 < 2**30
            if n_counter == counter(1<<i):
                return True
        return False
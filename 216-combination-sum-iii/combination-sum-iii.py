class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        bs = []
        # def answer(ind,s):
        #     if len(bs) == k:
        #         if s == 0:
        #             ans.append(bs.copy())
        #             return
        #     if n<=0:
        #         return
        #     for i in range(ind , 10):
        #         if i > s:
        #             break
        #         bs.append(i)
        #         answer(i+1, s-i)
        #         bs.pop()
        
        def answer(s = 1, n = n , ds= []):
            if len(ds) == k and n == 0:
                ans.append(ds)
                return
            if n < 0 or len(ds) > k:
                return
            
            for i in range(s,10):
                if n < i:
                    break
                else:
                    answer(i+1,n-i , ds+[i])


        answer(1,n)
        return ans

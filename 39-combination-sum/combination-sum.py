
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        # def answer(i,s):
        #     # nonlocal ans ,ds
        #     if s > target or i == len(candidates):
        #         return
        #     if s == target:
        #         ans.append(ds.copy())
        #         return
        #     ds.append(candidates[i])
        #     answer(i,s+candidates[i])
        #     ds.pop()
        #     answer(i+1,s)
        # answer(0,0)

#--------------------------------------------------------
        def answer(i, target):
            if i == len(candidates):
                if target == 0:
                    ans.append(ds.copy())
                    return
                return
            if candidates[i] <= target:
                ds.append(candidates[i])
                answer(i , target - candidates[i])
                ds.pop()
            answer(i+1 , target)
        answer(0,target)

        return ans

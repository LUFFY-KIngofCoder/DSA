
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        def answer(i,s):
            # nonlocal ans ,ds
            if s > target or i == len(candidates):
                return
            if s == target:
                ans.append(ds.copy())
                return
            ds.append(candidates[i])
            answer(i,s+candidates[i])
            ds.pop()
            answer(i+1,s)
        answer(0,0)
        return ans

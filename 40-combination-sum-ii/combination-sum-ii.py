class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        # ds = []
        def answer(ind, target,ds=[]):
            if target == 0:
                ans.append(ds) 
                return
            for i in range(ind,len(candidates)):
                if i > ind and candidates[i] == candidates[i-1]:
                    continue
                if candidates[i] > target:
                    break
                # ds.append(candidates[i])
                answer(i+1 , target - candidates[i],ds+[candidates[i]])
                # ds.pop()
        answer(0,target)

        return ans
# 1,1,2,5,6,7,10
# 0,1,2,3,4,5,6
# target=8-1=7
# ds = [1,]
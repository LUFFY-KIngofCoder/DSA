class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        # def answer(ind,ds = []):
            
        #     ans.append(ds)
                
        #     for i in range(ind, len(nums)):
        #         if i!=ind and nums[i] == nums[i-1]:
        #             continue
        #         answer(i+1,ds+[nums[i]])
        # answer(0)

        def answer(ind , ds=[]):
           
            ans.append(ds)
            
            
            for i in range(ind,len(nums)):
                if i == ind or (i!= 0 and nums[i] != nums[i-1]):    
                    answer(i+1 ,ds+[nums[i]])

        answer(0)

        return ans
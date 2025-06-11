class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height) - 1
        max_water = 0
        
        while(i < j):
            l = min(height[i] , height[j])
            b = j-i
            max_water = max(max_water,l*b)

            if height[i] < height[j]:
                i+=1
            else:
                j-=1
        return max_water
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        l_max = [0]*n
        r_max = [0]*n
        water = 0
        l_max[0] = height[0]
        r_max[-1] = height[-1]
        
        for i in range(1,n):

            l_max[i] = max(l_max[i-1],height[i])
            r_max[n-1-i] = max(r_max[n-1-i+1],height[n-i-1])

        for i in range(n):
            if height[i] < l_max[i] and height[i]<r_max[i]:
                water+= min(l_max[i],r_max[i]) - height[i]
        return water

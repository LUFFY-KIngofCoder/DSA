class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a= [intervals[0]]
        n = len(intervals)
       
        for i in range(1,n):
            if intervals[i][0] > a[-1][1]:
                a.append(intervals[i])
           
            else:
                a[-1][1] = max(intervals[i][1],a[-1][1])
        
        return a
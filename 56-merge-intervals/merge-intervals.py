class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        a= [intervals[0]]
        n = len(intervals)
        j=0
        for i in range(1,n):
            if intervals[i][0] >= a[j][0] and intervals[i][0] <= a[j][1]:
                a[j][1] = max(intervals[i][1],a[j][1])
            else:
                a.append(intervals[i])
                j+=1
        
        return a
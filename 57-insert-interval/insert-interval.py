class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0
        n = len(intervals)

        while n > i and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        merged = [newInterval[0], newInterval[1]]
        while n > i and intervals[i][0] <= merged[1]:
            merged[0] = min(merged[0], intervals[i][0])
            merged[1] = max(merged[1], intervals[i][1])
            i += 1
        res.append(merged)

        while n > i:
            res.append(intervals[i])
            i += 1
        
        return res
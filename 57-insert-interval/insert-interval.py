class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)

        #
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1
        
        #
        merged = [newInterval[0], newInterval[1]]
        while i < n and intervals[i][0] <= merged[1]:
            merged[0] = min(intervals[i][0], merged[0])
            merged[1] = max(intervals[i][1], merged[1])
            i += 1
        result.append(merged)

        #
        while i < n:
            result.append(intervals[i])
            i += 1
        
        return result
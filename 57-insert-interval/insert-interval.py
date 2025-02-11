class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        i = 0
        n = len(intervals)
        # add all elements that end before our N_interval starts
        while i < n and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i += 1

        # check for overlapping intervals and merge if necessary
        merged = [newInterval[0], newInterval[1]]
        while i < n and intervals[i][0] <= merged[1]:
            merged[0] = min(intervals[i][0], merged[0])
            merged[1] = max(intervals[i][1], merged[1])
            i += 1
        result.append(merged)

        # add the rest of intervals that start after our N_interval ends
        while i < n:
            result.append(intervals[i])
            i += 1
        
        # return our intevals
        return result
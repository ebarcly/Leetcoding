class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merged = []
        for interval in range(len(intervals)):
            if len(merged) == 0 or merged[-1][1] < intervals[interval][0]:
                merged.append(intervals[interval])
            else:
                merged[-1][1] = max(merged[-1][1],intervals[interval][1])
        return merged

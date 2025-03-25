from collections import Counter
from heapq import heappush, heappop
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,2,3] k = 2 
        # 1: 3, 2: 2, 3: 1
        freq = Counter(nums)
        min_heap = []

        for n, f in freq.items():
            heappush(min_heap, (f, n))
            if len(min_heap) > k:
                heappop(min_heap)
        return [v[1] for v in min_heap]
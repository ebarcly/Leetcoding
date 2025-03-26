class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # [1,1,1,2,2,3] k = 2
        # 1: 3, 2: 2, 3: 1

        freq = Counter(nums)
        min_heap = []

        for num, freq in freq.items():
            heapq.heappush(min_heap, (freq, num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        return [pair[1] for pair in min_heap]

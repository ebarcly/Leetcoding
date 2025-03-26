class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_ct = Counter(nums)

        min_hp = []

        for num, freq in freq_ct.items():
            heapq.heappush(min_hp, (freq, num))
            if len(min_hp) > k:
                heapq.heappop(min_hp)
        
        return [v[1] for v in min_hp]
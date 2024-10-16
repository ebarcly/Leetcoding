class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        sort_freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            freq[i] = 1 + freq.get(i, 0)
        
        for n, v in freq.items():
            sort_freq[v].append(n)

        res = []
        for i in range(len(sort_freq) -1, 0, -1):
            for n in sort_freq[i]:
                res.append(n)
            if len(res) == k:
                return res
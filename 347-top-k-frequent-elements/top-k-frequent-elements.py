class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_counter = {}
        sort_freq = [[] for i in range(len(nums) + 1)]

        # output list
        result = []

        # hash elements to the ht
        for n in nums:
            freq_counter[n] = 1 + freq_counter.get(n, 0)
        # sorting elements
        for i, v in freq_counter.items():
            sort_freq[v].append(i)

        for i in range(len(sort_freq) - 1, 0, -1):
            for n in sort_freq[i]:
                result.append(n)
                if len(result) == k:
                    return result

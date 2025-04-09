class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums) # O(n) time 
        longest = 0

        # O(n)
        for n in numSet:
            if (n - 1) not in numSet:
                length = 1
                while (n + length) in numSet:
                    length += 1
                longest = max(length, longest)
        
        return longest

        # space O(n)
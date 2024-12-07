class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Boyer-Moore voting algorithm
        # O(1) Space as requested
        candidate = nums[0]
        count = 1

        for num in nums[1:]:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate


        # # Using hashmap - O(n) space

        # counts = {}

        # for i in nums:
        #     counts[i] = counts.get(i, 0) + 1

        #     if counts[i] > len(nums) // 2:
        #         return i
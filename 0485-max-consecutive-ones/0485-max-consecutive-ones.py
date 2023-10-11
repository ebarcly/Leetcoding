class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = count = 0
        for num in nums:
            if num == 1:
                count += 1
            if num == 0 or num == len(nums):
                if count > maximum:
                    maximum = count
                count = 0
        if count > maximum:
            maximum = count
        return maximum
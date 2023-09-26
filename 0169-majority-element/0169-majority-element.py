class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Boyer-Moore Voting Algorithm.
        """
        candidate = 0
        counter = 0

        for i in nums:
            if counter == 0:
                candidate = i
            if i == candidate:
                counter += 1
            else:
                counter -= 1
        return candidate
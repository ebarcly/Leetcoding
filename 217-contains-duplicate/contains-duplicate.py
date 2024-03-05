class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums2 = set(nums)
        return len(nums) != len(nums2)
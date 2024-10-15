class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        unique = set(nums)

        return True if len(unique) != len(nums) else False
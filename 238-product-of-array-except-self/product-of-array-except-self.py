class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = [1] * len(nums)

        for i in range(1, len(nums)):
            product[i] = product[i - 1] * nums[i  - 1]
        
        right = nums[-1]
        for n in range(len(nums) - 2, -1, -1):
            product[n] *= right
            right *= nums[n]
        return product
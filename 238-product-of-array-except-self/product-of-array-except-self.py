class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
                                    # 1[1,2,3,4]1
        product = [1] * len(nums)  # prefix -> [1,1,6,24] sufixes <- [1,1,6,24]

        for n in range(1, len(nums)):
            product[n] = product[n - 1] * nums[n - 1]
        
        right = nums[-1]
        for i in range(len(nums) -2, -1, -1):
            product[i] *= right
            right *= nums[i]
        return product
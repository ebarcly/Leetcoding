class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # ans = []
        # postfix = 24
        
        length = len(nums)
        ans = [1] * length
        
        for i in range(1, length):
            ans[i] = ans[i-1] * nums[i-1]
        
        postfix = 1
        for i in reversed(range(length)):
            ans[i] *= postfix
            postfix *= nums[i]
        
        return ans
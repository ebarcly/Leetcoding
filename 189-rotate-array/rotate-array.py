class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # handle k rotation
        if k > len(nums):
            k = k % len(nums)
        
        # helper func
        def swap(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # rotate array
        swap(0, len(nums) - 1)

        # rotate k elements
        swap(0, k - 1)

        # rotate n - k elements
        swap(k, len(nums) - 1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # handle k > nums
        if k > len(nums):
            k = k % len(nums)
        
        # helper function
        def swap(start: int, end: int) -> None:
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
        
        # swap entire array
        swap(0, len(nums) - 1)

        # swap k elements
        swap(0, k - 1)

        # swap nums - k
        swap(k, len(nums) - 1)
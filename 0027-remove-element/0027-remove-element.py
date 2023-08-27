class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0  # slow pointer 

        for j in range(len(nums)):  # fast pointer
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
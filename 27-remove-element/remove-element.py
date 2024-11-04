class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Use slow pointer and fast pointer to sort the list by the condition
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        return i
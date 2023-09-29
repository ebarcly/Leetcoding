class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, mapping = [], {}

        # Iterate over nums2 to populate the mapping
        for num in nums2:
          while stack and stack[-1] < num:
            mapping[stack.pop()] = num
          stack.append(num)

        # For elements in nums1, find the next greater element from the mapping
        return [mapping.get(num, -1) for num in nums1]


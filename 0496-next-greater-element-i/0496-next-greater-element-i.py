class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []

        for num in nums1:
          found = False
          start_index = nums2.index(num) if num in nums2 else 0
          for j in range(start_index, len(nums2)):
            if nums2[j] > num:
              result.append(nums2[j])
              found = True
              break
          if not found:
            result.append(-1)
        return result

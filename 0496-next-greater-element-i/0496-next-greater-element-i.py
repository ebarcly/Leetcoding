class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater = []

        for i in range(len(nums1)):
          found = False
          for j in range(len(nums2)):
            if found and nums2[j] > nums1[i]:
              greater.append(nums2[j])
              break
            if nums1[i] == nums2[j]:
              found = True
          else:
            greater.append(-1)
        return greater
        
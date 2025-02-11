class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = {}

        for i, v in enumerate(nums):
            dif = target - v
            if dif in res:
                return [i, res[dif]]
            res[v] = i
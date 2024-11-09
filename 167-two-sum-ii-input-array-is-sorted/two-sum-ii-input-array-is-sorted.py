class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ans = []
        i = 0
        j = len(numbers) - 1

        for _ in range(len(numbers)):
            if numbers[i] + numbers[j] == target:
                ans.append(i + 1)
                ans.append(j + 1)
                return ans
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                i += 1

class Solution:
    def jump(self, nums: List[int]) -> int:
        currEnd = 0
        max_reach = 0
        jumps = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])

            if i == currEnd:
                jumps += 1
                currEnd = max_reach
        
        return jumps
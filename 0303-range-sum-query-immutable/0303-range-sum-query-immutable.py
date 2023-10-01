class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = []
        currentSum = 0
        for i in nums:
            currentSum += i
            self.prefixSum.append(currentSum)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.prefixSum[right]
        else:
            return self.prefixSum[right] - self.prefixSum[left - 1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
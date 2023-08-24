class Solution:
    def numberOfSteps(self, num: int) -> int:
        # count the number of 1s and 0s in binary representation of num
        return bin(num).count('1') - 1 + len(bin(num)) - 2
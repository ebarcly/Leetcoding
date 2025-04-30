class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []

        for token in tokens:
            if len(token) > 1 or token.isdigit():
                nums.append(int(token))
            else:
                if token == "+":
                    nums[-2] += nums[-1]
                elif token == "-":
                    nums[-2] -= nums[-1]
                elif token == "*":
                    nums[-2] *= nums[-1]
                else:
                    nums[-2] = int(float(nums[-2]) / nums[-1])
                nums.pop()
        return nums[0]

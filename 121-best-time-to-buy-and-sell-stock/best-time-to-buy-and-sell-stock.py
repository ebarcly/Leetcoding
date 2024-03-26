class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0

        left = prices[0]

        for right in prices:
            if right < left:
                left = right
            elif right - left > max_profit:
                max_profit = right - left
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_val = prices[0]

        for price in prices:
            if price < min_val:
                min_val = price
            max_profit = max(max_profit, price - min_val)
        
        return max_profit
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        min_p = prices[0] # 7, # 1

        for price in prices:
            if price < min_p:
                min_p = price
            cur = price - min_p
            if cur > total:
                total = cur
        return total
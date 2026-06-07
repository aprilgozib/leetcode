class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_profit = 0
        for today in prices:
            min_price = min(min_price, today)
            max_profit = max(max_profit, today - min_price)
        return max_profit
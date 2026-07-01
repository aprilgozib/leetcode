class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # find min price, max profit
        min_price = float('inf')
        max_profit = 0
        for today in prices:
            min_price = min(min_price, today)
            max_profit = max(max_profit, today - min_price)
        return max_profit
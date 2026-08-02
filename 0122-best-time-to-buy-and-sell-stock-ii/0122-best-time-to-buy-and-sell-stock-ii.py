class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        yesterday = prices[0]
        for today in prices[1:]:
            if today > yesterday:
                total += today - yesterday
            yesterday = today

        return total

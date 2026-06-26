class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if today > yesterday -> total += today - yesterday
        yesterday = prices[0]
        total = 0
        for i in range(1, len(prices)):
            today = prices[i]
            if today > yesterday:
                total += today - yesterday
            yesterday = prices[i]
        return total
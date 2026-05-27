class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # total, today, yesterday
        total = 0
        for i in range(1, len(prices)):
            yesterday = prices[i-1]
            today = prices[i]
            if today > yesterday:
                total += today - yesterday
        return total

        
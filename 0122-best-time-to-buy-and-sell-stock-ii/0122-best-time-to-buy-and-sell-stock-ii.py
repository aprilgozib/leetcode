class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # yesterday < today -> total += today - yesterday
        yesterday = prices[0]
        total = 0

        for today in prices[1:]:
            if today > yesterday:
                total += today - yesterday
            yesterday = today

        return total
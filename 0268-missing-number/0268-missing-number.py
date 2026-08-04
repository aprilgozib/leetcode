class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum = 0
        for num in nums:
            sum += num
        total = len(nums) * (len(nums) + 1) // 2
        if total == sum:
            return 0
        else:
            return total - sum

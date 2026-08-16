class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            total += num

        sum = len(nums) * (len(nums) + 1) // 2

        return sum - total
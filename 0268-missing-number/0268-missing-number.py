class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sort -> compare
        # compare total and sum
        total = len(nums) * (len(nums) + 1) // 2
        return total - sum(nums)
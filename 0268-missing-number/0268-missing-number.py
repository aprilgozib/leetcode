class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)

        # total - sum
        # return len(nums) * (len(nums) + 1) // 2 - sum(nums)
class Solution:
    def rob(self, nums: List[int]) -> int:
        # compare prev2 + curr vs prev1
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(prev2 + num, prev1)
            prev2 = prev1
            prev1 = curr

        return curr
class Solution:
    def rob(self, nums: List[int]) -> int:
        # use prev2, prev1 -> prev1 compare prev2 + num
        if len(nums) == 1:
            return nums[0]

        prev2, prev1 = 0, 0
        for num in nums:
            curr = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = curr
        return curr
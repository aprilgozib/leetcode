class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if curr_sum + i < i -> reset
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in nums[1:]:
            curr_sum = max(curr_sum + i, i) # i is bigger -> restart
            max_sum = max(curr_sum, max_sum)

        return max_sum
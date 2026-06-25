class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if the sum - occur -> restart
        curr_sum = nums[0]
        max_sum = nums[0]
        for i in nums[1:]:
            curr_sum = max(curr_sum + i, i) # if - occur restart
            max_sum = max(max_sum, curr_sum)
        return max_sum
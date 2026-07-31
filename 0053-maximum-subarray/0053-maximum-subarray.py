class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # if minus -> reset
        curr_sum = nums[0]
        max_sum = nums[0]

        for i in nums[1:]:
            curr_sum = max(curr_sum + i, i) # i is bigger if minus occur
            max_sum = max(max_sum, curr_sum)

        return max_sum
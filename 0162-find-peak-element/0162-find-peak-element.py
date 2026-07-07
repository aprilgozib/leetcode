class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # binary search
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) - 1
            if nums[mid] < nums[mid + 1]: # peak is on the right
                left = mid + 1
            else: # peak is on the left
                right = mid
        return left
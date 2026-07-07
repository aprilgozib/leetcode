class Solution:
    def findMin(self, nums: List[int]) -> int:
        # binary search
        # left, right sorted part
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # minimum is on the right:
                left = mid + 1
            else: # minimum is on the left
                right = mid
        return nums[left]
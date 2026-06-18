class Solution:
    def findMin(self, nums: List[int]) -> int:
        # using binary search
        # find sorted part ->
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]: # mininum is on the right
                left = mid + 1
            else: # minimun is on the left
                right = mid
        return nums[left]
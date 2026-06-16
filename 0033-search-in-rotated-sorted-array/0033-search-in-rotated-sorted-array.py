class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # using two pointer, focus on sorted part
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[left] <= nums[mid]: # left sorted
                if nums[left] <= target < nums[mid]: # target at left
                    right = mid - 1
                else: # target at right
                    left = mid + 1
            else: # right sorted
                if nums[mid] < target <= nums[right]: # target at right
                    left = mid + 1
                else: # target at left
                    right = mid - 1
        return -1

        return -1
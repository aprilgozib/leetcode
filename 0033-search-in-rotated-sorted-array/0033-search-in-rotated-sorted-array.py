class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use two pointer, binary search
        # focus on the sorted part
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] <= nums[mid]: # left sorted
                if nums[left] <= target <= nums[mid]: # left part
                    right = mid - 1
                else: # right part
                    left = mid + 1
            else: # right sorted
                if nums[mid] <= target <= nums[right]: # right part
                    left = mid + 1
                else: # left part
                    right = mid - 1
        return -1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the sorted part
        # target located where 
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid

            elif nums[left] <= nums[mid]: # left sorted
                if nums[left] <= target <= nums[mid]: # target located left
                    right = mid - 1
                else: # target located right
                    left = mid + 1
            
            else: # right sorted
                if nums[mid] <= target <= nums[right]: # target located right
                    left = mid + 1
                else: # target located left
                    right = mid - 1
        return -1 
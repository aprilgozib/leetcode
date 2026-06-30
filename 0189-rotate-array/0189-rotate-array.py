class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # slicing
        # if k is bigger then len(nums)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
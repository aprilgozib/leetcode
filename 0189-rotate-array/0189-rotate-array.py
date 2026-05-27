class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # slicing
        # [1,2] k = 7 <- we need k = k % len(nums)
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]

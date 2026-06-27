class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swith
        if len(nums) < 2:
            return nums
        # two pointers
        left, right = 0, 1
        while right < len(nums):
            if nums[left] == 0:
                if nums[right] == 0: # 0, 0
                    right += 1
                else: # 0, 1 -> 1, 0
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
            else: # 1,
                left += 1
                right += 1
            

            
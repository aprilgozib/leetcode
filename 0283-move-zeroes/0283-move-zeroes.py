class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # while, two point
        if len(nums) < 2:
            return nums

        left, right = 0, 1
        while right < len(nums): #0,1,0,3,12 -> 1,0,0,3,12 -> 1,3,0,0,12
            if nums[left] == 0:
                if nums[right] == 0:
                    right += 1
                else:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right += 1
            else:
                left += 1
                right += 1
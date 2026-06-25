class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        c = 1
        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]: # 0,1 1,2 2,3
                nums[c] = nums[i] #
                c += 1
        return c
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        p = 1
        if len(nums) == 0:
            return 0

        for i in range(1, len(nums)): # 1,2,3,4
            if nums[i-1] != nums[i]:
                nums[p] = nums[i]
                p += 1
        return p
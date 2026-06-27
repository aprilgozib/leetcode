class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # use dictionary
        # set -> compare len
        s = set(nums)
        return True if len(nums) != len(s) else False
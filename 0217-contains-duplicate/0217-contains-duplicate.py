class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # using set and compare the length
        com = set(nums)
        if len(com) != len(nums):
            return True
        else:
            return False

        # using dict
        #seen = {}
        #for i in nums:
        #    seen[i] = seen.get(i, 0) + 1
        
        #for count in seen.values():
        #    if count > 1:
        #        return True
        #return False
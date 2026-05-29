class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # using dict -> O(n) space complexity
        #seen = {}
        #for i in nums:
        #    seen[i] = seen.get(i, 0) + 1
        
        #for key, value in seen.items():
        #    if value == 1:
        #        return key

        # using xor -> space complexity O(1)
        res = 0
        for i in nums:
            res ^= i
        return res
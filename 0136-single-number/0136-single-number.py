class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for ch in nums:
            seen[ch] = seen.get(ch, 0) + 1
        for key, value in seen.items():
            if value == 1:
                return key
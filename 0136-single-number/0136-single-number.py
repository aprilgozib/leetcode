class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {} #{2:2, 1:1}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1
        for value, count in seen.items():
            if count == 1:
                return value
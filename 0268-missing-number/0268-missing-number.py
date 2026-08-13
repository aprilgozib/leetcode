class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for i in range(len(nums)):
            if i not in seen:
                return i
            
        return len(nums)
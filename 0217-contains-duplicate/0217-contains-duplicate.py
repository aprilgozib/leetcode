class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            seen[num] = seen.get(num, 0) + 1

        for count in seen.values():
            if count > 1:
                return True

        return False
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        seen = {}
        res = []
        for num in nums1:
            seen[num] = seen.get(num, 0) + 1
        for num in nums2:
            if num in seen:
                res.append(num)
        return res
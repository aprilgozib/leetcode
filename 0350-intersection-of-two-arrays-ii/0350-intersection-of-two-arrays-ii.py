class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for num in nums1:
            seen[num] = seen.get(num, 0) + 1

        # seen = {1:2, 2:2}
        res = []
        for num in nums2:
            if num in seen and seen[num] > 0:
                res.append(num)
                seen[num] -= 1

        return res
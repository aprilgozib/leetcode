class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {}
        for i in nums1:
            seen[i] = seen.get(i, 0) + 1

        res = []
        for i in nums2:
            if i in seen and seen[i] > 0:
                res.append(i)
                seen[i] -= 1

        return res
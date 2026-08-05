class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = {} # 1:1, 2:1
        for i in nums1:
            if i not in seen:
                seen[i] = 1
            else:
                continue

        res = []
        for i in nums2:
            if i in seen and seen[i] > 0:
                res.append(i)
                seen[i] -= 1

        return res
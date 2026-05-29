class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # using dict
        seen = {}
        for i in nums1:
            seen[i] = seen.get(i, 0) + 1

        res = []
        
        for j in nums2:
            if j in seen and seen[j] > 0:
                res.append(j)
                seen[j] -= 1
        
        return res
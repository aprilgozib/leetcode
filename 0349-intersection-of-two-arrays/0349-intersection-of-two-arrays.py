class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # use set
        s1 = set(nums1) # 1,2
        s2 = set(nums2) # 2
        return list(s1 & s2)
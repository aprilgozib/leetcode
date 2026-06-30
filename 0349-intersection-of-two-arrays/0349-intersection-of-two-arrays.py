class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # dictionary -> enumerate, items(), values()
        # set -> & intersection
        # two pointers -> move left to right
        nums1.sort()
        nums2.sort()
        res = []
        left, right = 0, 0
        while left < len(nums1) and right < len(nums2):
            if nums1[left] == nums2[right]:
                res.append(nums1[left])
                left += 1
                right += 1
                # [1,1,2,2] duplicate
                while left < len(nums1) and nums1[left] == nums1[left - 1]:
                    left += 1
                while right < len(nums2) and nums2[right] == nums2[right - 1]:
                    right += 1
            elif nums1[left] < nums2[right]:
                left += 1
            else:
                right += 1
        return res
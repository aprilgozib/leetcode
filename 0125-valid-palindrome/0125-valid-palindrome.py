class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use isalnum, two pointer
        new = []
        for ch in s:
            if ch.isalnum():
                new.append(ch.lower())
        left, right = 0, len(new) - 1
        while left < right:
            if new[left] == new[right]:
                left += 1
                right -= 1
            else:
                return False
        return True
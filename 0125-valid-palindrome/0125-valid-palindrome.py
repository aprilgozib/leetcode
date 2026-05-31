class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use isalnum, two pointer 
        new = []
        for ch in s:
            if ch.isalnum():
                new.append(ch.lower())
        
        left = 0
        right = len(new) - 1
        while left < right:
            if new[left] != new[right]:
                return False
            left += 1
            right -= 1
        return True
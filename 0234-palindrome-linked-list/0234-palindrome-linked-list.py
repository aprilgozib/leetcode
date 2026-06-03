# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # use slow, fast
        # find the middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next # 2
            fast = fast.next.next # 1

        # flip the back part
        # 1, 2, 1, 2
        prev = None
        curr = slow
        while curr: 
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        # compare front and back
        front = head
        back = prev
        while back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.next

        return True
        

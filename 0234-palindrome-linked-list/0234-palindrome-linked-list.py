# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # slow, fast -> find middle and back
        # flip back part
        # compare front and middle
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # middle = slow, end = fast
        prev = None
        curr = slow
        while curr:
            next_node = curr.next
            curr.next = prev
            prev =  curr
            curr = next_node

        # compare front and back(middle)
        front = head
        back = prev
        while back:
            if front.val != back.val:
                return False
            front = front.next
            back = back.next

        return True
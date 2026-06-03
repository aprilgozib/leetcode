# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # prev, curr, next_node
        prev = None
        curr = head
        while curr:
            next_node = curr.next # 2
            curr.next = prev # None
            prev = curr # 1
            curr = next_node # 2

        return prev
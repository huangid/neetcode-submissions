# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        length = 0
        dummy = ListNode(next=head)
        p = dummy
        while p.next:
            length += 1
            p = p.next
        k = k % length
        k = length - k
        left = head
        for i in range(k):
            p.next = ListNode(left.val)
            left = left.next
            p = p.next
        return left
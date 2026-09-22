# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p = dummy
        p2 = None
        for _ in range(left):
            p2 = p
            p = p.next
        pre = None
        p1 = p
        for _ in range(right - left + 1):
            nxt = p.next
            p.next = pre
            pre = p
            p = nxt
        p1.next = p
        p2.next = pre
        return dummy.next
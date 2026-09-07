# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)
        fast = slow = dummy
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        mid = slow.next
        slow.next = None
        pre = None
        cur = mid
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        p1 = dummy.next
        p2 = pre
        ans = ListNode()
        p = ans
        while p2:
            p.next = p1
            p = p.next
            p1 = p1.next
            p.next = p2
            p = p.next
            p2 = p2.next
        p.next = p1




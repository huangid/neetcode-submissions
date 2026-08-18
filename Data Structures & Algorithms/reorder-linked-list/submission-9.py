# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        ptr = slow.next
        slow.next = None
        pre = None
        cur = ptr
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        ptr = pre
        ptr0 = head
        while ptr:
            nxt = ptr.next
            nxt0 = ptr0.next
            ptr0.next = ptr
            ptr.next = nxt0
            ptr = nxt
            ptr0 = nxt0


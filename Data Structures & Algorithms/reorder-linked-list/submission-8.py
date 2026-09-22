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
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None
        pre = None
        while second:
            nxt = second.next
            second.next = pre
            pre = second
            second = nxt
        second = pre
        first = head
        while second:
            nxt1, nxt2 = first.next, second.next
            first.next = second
            first.next.next = nxt1
            first = nxt1
            second = nxt2



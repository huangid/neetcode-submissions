# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        sort = ListNode()
        p1 = head
        while p1:
            v = p1.val
            p2 = sort
            while p2.next and p2.next.val < v:
                p2 = p2.next
            node = ListNode(val=v, next=p2.next)
            p2.next = node
            p1 = p1.next
        return sort.next
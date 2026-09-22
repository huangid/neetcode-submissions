# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        p = head
        def insert(pr):
            node = ListNode(p.val, next=None)
            while pr.next and pr.next.val < node.val:
                pr = pr.next
            node.next = pr.next
            pr.next = node
        while p:
            pr = res
            insert(pr)
            p = p.next
        return res.next
            
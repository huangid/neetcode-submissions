# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        p1 = list1
        p2 = list2
        dummy = ListNode()
        pm = dummy
        while p1 and p2:
            if p1.val < p2.val:
                pm.next = p1
                p1 = p1.next
            else:
                pm.next = p2
                p2 = p2.next
            pm = pm.next
        if p1:
            pm.next = p1
        if p2:
            pm.next = p2
        return dummy.next
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pm = dummy
        while list1 and list2:
            if list1.val < list2.val:
                pm.next = list1
                list1 = list1.next
            else:
                pm.next = list2
                list2 = list2.next
            pm = pm.next
        if list1:
            pm.next = list1
        if list2:
            pm.next = list2
        return dummy.next
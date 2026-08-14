# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        merge = dummy
        while list1 and list2:
            if list1.val < list2.val:
                merge.next = list1
                merge = merge.next
                list1 = list1.next
            else:
                merge.next = list2
                merge = merge.next
                list2 = list2.next
        if list1:
            merge.next = list1
            merge = merge.next
            list1 = list1.next
        if list2:
            merge.next = list2
            merge = merge.next
            list2 = list2.next
        return dummy.next
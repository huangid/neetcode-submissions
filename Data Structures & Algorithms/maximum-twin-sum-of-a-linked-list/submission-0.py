# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        p1 = ListNode(next=head)
        p2 = ListNode(next=head)
        arr = []
        n = 0
        while p1 and p1.next:
            p1 = p1.next.next
            p2 = p2.next
            n += 1
            arr.append(p2.val)
        p2 = p2.next
        while p2:
            n = n - 1
            arr[n] += p2.val
            p2 = p2.next
        return max(arr)
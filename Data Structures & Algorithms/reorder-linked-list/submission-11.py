class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        dummy = ListNode(next=head)
        f = s = dummy
        while f and f.next:
            f = f.next.next
            s = s.next
        mid = s.next
        s.next = None

        pre = None
        while mid:
            nxt = mid.next
            mid.next = pre
            pre = mid
            mid = nxt

        p1, p2 = head, pre
        while p2:
            n1, n2 = p1.next, p2.next
            p1.next = p2
            p2.next = n1
            p1, p2 = n1, n2

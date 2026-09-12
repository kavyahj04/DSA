def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        curr = head
        while n > 0 and curr:
            curr = curr.next
            n -= 1
        left = dummy
        while curr:
            left = left.next
            curr = curr.next 
        left.next = left.next.next
        return dummy.next
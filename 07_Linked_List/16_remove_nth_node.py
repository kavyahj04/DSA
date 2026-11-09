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

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        slow = dummy
        dummy.next = head
        curr  = head
        cnt = 0
        while curr:
            cnt += 1
            if cnt > n and dummy.next:
                slow = slow.next
            curr = curr.next
        slow.next = slow.next.next
        return dummy.next


class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head

        first = dummy
        second = dummy

        for i in range(n + 1):
            first = first.next

        while first:
            first = first.next
            second = second.next

        second.next = second.next.next

        return dummy.next
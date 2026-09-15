def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        vals = []
        curr = head
        while curr:
            vals.append(curr.val)
            curr = curr.next
        vals.sort()
        curr = head
        for val in vals:
            curr.val = val
            curr = curr.next
        return head
def addOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return ListNode(1)
    prv = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt

    reversed_head = prv
    curr = reversed_head
    carry = 1
    while curr or carry:
        total = curr.val + carry
        carry = total // 10
        curr.val = total % 10

        if not curr.next and carry:
            curr.next = ListNode(carry)
            carry = 0
        curr = curr.next

    prv = None
    curr = reversed_head
    while curr:
        nxt = curr.next
        curr.next = prv
        prv = curr
        curr = nxt
    return prv
    
        
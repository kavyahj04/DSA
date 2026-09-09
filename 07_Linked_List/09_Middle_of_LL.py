def middleOfLinkedList(head):
    slow, fast = head, head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    if fast.next == None:
        return slow
    else:
        slow = slow.next
        return slow

def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
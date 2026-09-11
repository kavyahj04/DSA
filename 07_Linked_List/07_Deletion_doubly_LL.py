def deleteAtStart(head):
    if head is None or head.next is None:
        return None
    
    head = head.next
    head.prev = None  # Extra step for DLL!
    return head


def deleteAtEnd(head):
    if head is None or head.next is None:
        return None
    
    temp = head
    while temp.next:
        temp = temp.next
        
    # temp is now at the last node
    temp.prev.next = None  # Sever the forward link from the 2nd-to-last node
    return head
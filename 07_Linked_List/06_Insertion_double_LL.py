# 1.Insert at Start

def insertAtStart(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    
    new_node.next = head
    head.prev = new_node  # Extra step for DLL!
    return new_node



#2. Insert at End

def insertAtEnd(head, val):
    new_node = Node(val)
    if head is None:
        return new_node
    
    temp = head
    while temp.next:
        temp = temp.next
        
    temp.next = new_node
    new_node.prev = temp  # Extra step for DLL!
    return head
    
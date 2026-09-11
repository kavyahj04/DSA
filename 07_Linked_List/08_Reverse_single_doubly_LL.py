# Reverse Single linked list

class Node:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

def reverseDLL(head):
    if head is None or head.next is None:
        return head
    
    curr = head
    temp = None
    
    while curr:
        # 1. Swap next and prev pointers for current node
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        
        # 2. Move to the next node in original list
        # (Since we swapped next and prev, curr.prev points to the original next node!)
        curr = curr.prev
        
    # temp now points to the second-to-last node of the original list,
    # so temp.prev is the new head of the reversed list.
    return temp.prev

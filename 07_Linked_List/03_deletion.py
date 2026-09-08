class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)


# 1 delete first node

def deleteFirst(head):
    if head is None:
        return None
    return head.next

# T(n) - O(1)

# 2 delete Last Element

def deleteLast(head):
    temp = head
    if temp is None:
        return None
    if temp.next is None:
        return None
    while temp.next.next is not None:
        print(temp.val)
        temp = temp.next
    temp.next = None
    return temp
deleteLast(head)

# T(n) - O(n)
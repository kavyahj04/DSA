

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)


# 1. Insert at Start 

def InsertAtStart(head, num):
    temp = head
    head = Node(num)
    head.next = temp

    # Test
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next
# InsertAtStart(head, 1)

# Or

def insertAtHead(self, head, newData):
        # Create a new node whose next points to current head
        newNode = Node(newData, head)
        # Return the new node as the head
        return newNode
# T(n) - O(1)

# 2. Insert at end

def InsertAtEnd(head, num):
    temp = head
    new_node = Node(num)
    while temp.next:
        temp = temp.next
    temp.next = new_node
    temp = head
    while temp:
        print(temp.val)
        temp = temp.next

    
InsertAtEnd(head, 1)
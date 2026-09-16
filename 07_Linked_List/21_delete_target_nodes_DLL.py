def deleteLinkedList(head, target):
    curr = head
    while curr:
        if curr.val == target:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = head.next
            if curr.next:
                    curr.next.prev = curr.prev
        curr = curr.next
    print(curr)
    return head

class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev
    
head = Node(2)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(1)
node6 = Node(1)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6

node2.prev = head
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5

def print_list(node):
    elements = []
    while node:
        elements.append(str(node.val))
        node = node.next
    print(" -> ".join(elements))

head = deleteLinkedList(head, 1)
print_list(head)
def removedup(head):
    curr = head
    val = float("-inf")
    while curr:
        if curr.val != val:
            val = curr.val
        else:
            if curr.prev:
                curr.prev.next = curr.next
            else:
                head = curr.next
            if curr.next:
                curr.next.prev = curr.prev
        curr = curr.next
    return head



class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev
    
head = Node(0)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(3)
node6 = Node(5)
node7 = Node(5)


head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7

node2.prev = head
node3.prev = node2
node4.prev = node3
node5.prev = node4
node6.prev = node5
node7.prev = node6

def print_list(node):
    elements = []
    while node:
        elements.append(str(node.val))
        node = node.next
    print(" -> ".join(elements))

head = removedup(head)
print_list(head)
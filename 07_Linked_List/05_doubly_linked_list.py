class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev
    
head = Node(2)
node2 = Node(3)
node3 = Node(4)
node4 = Node(5)


head.next = node2
node2.next = node3
node3.next = node4

node2.prev = head
node3.prev = node2
node4.prev = node3

# (Alternative clean creation using a helper function)
def create_doubly_linked_list(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        new_node = Node(val, prev=curr)
        curr.next = new_node
        curr = new_node
    return head

# Create directly from list: 2 -> 3 -> 4 -> 5
head = create_doubly_linked_list([2, 3, 4, 5])
def findSumPair(head, s):
    left = head
    right = head
    if not head: return []
    while right.next:
        right = right.next
    
    pairs = []
    while left.val <= right.val:
        temp = left.val + right.val
        if temp == s:
            pairs.append([left.val, right.val])
            left = left.next
            right = right.prev
        elif temp < s:
            left = left.next
        else:
            right = right.prev
    print(pairs)








class Node:
    def __init__(self, val, next = None, prev = None):
        self.val = val
        self.next = next 
        self.prev = prev
    
head = Node(0)
node2 = Node(1)
node3 = Node(2)
node4 = Node(3)
node5 = Node(4)
node6 = Node(5)
node7 = Node(6)


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

findSumPair(head, 5)
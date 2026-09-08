
# 1. Creation 

class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)

# 2. Traversal
temp = head
while temp:
    print(temp.val)
    temp = temp.next

# T(n) => O(n)


# 3. Length of the list

temp = head
cnt = 0
while temp:
    cnt += 1
    temp = temp.next
print(f"The length of the linked list is - {cnt}")

# 4.Searching for a value.abs
temp = head

while temp:
    if temp.val == 3:
        print("Value found")
    temp = temp.next
print("Value not found")
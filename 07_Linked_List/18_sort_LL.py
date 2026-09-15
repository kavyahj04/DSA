class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def sort_linked_list(self, head:ListNode) -> ListNode:
        if not head or not head.next:
            return head
        left = head
        right = self.getMid(head)
        temp = right.next
        right.next = None
        right = temp

        left = self.sort_linked_list(left)
        right = self.sort_linked_list(right)

        return self.merge(left, right)

    
    def getMid(self, head):
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    
    def merge(self, left:ListNode, right:ListNode) -> ListNode:
        dummy = ListNode()
        tail = dummy

        while left and right:
            if left.val < right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        
        if left:
            tail.next = left
        if right:
            tail.next = right
        return dummy.next
# Helper function to print the linked list
def print_list(node):
    elements = []
    while node:
        elements.append(str(node.val))
        node = node.next
    print(" -> ".join(elements))

# Creating the dummy head node
lst = ListNode()

# Building your specified list: 6 -> 5 -> 1 -> 3 -> 2 -> 7 -> 0
lst.next = ListNode(6)
lst.next.next = ListNode(5)
lst.next.next.next = ListNode(1)
lst.next.next.next.next = ListNode(3)
lst.next.next.next.next.next = ListNode(2)
lst.next.next.next.next.next.next = ListNode(7)
lst.next.next.next.next.next.next.next = ListNode(0)

print("Original Linked List:")
print_list(lst.next)

# Sorting the linked list (passing the actual start node, lst.next)
sorted_head = lst.sort_linked_list(lst.next)

print("\nSorted Linked List:")
print_list(sorted_head)



class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reversekGrp(head, k):
    start = curr = head
    cnt = 0
    prev = None
    while curr:
        cnt += 1
        next_node = curr.next
        if cnt == k:
            head, prev = reverse(start, curr, prev, head)
            cnt = 0
        curr = next_node
    return head

def reverse(start, curr, prev,head):
    if prev:
        prev.next = curr
    else:
        head = curr

    next_prev = start

    group_end = curr.next

    p_prev = group_end
    p_curr = start

    while p_curr != group_end:
        p_next = p_curr.next
        p_curr.next = p_prev
        p_prev = p_curr
        p_curr = p_next
    return head, next_prev

# Helper function to print the linked list
def print_list(node):
    elements = []
    while node:
        elements.append(str(node.val))
        node = node.next
    print(" -> ".join(elements))


# Building your specified list: 6 -> 5 -> 1 -> 3 -> 2 -> 7 -> 0
lst = ListNode(1)
lst.next = ListNode(2)
lst.next.next = ListNode(3)
lst.next.next.next = ListNode(4)
lst.next.next.next.next = ListNode(5)
lst.next.next.next.next.next = ListNode(6)
lst.next.next.next.next.next.next = ListNode(7)
lst.next.next.next.next.next.next.next = ListNode(8)

print("Original Linked List:")
print_list(lst.next)

head = reversekGrp(lst, 3)

print_list(head)
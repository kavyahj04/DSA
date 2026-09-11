class Node:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


head = Node(2)
head.next = Node(3)
head.next.next = Node(4)
head.next.next.next = Node(5)
head.next.next.next.next = Node(6)
head.next.next.next.next.next = head.next.next


def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next 
        if slow == fast:
            cnt = 1
            slow = slow.next
            while slow != fast:
                slow = slow.next
                cnt += 1
            print(cnt)
            return cnt
    return None

detectCycle(head)
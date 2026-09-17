# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head
        n = 0
        # 1. Calculate length n
        curr = head
        while curr:
            n += 1
            curr = curr.next
            
        k = k % n
        if k == 0:
            return head

        # 2. Find split point (n - k steps)
        prev = None
        curr = head
        for _ in range(n - k):
            prev = curr
            curr = curr.next
            
        # Sever the link between the two parts
        prev.next = None
        
        # 3. Save reference to second list
        first_part = head   # Nodes 1 to n-k
        second_part = curr  # Nodes (n-k)+1 to n
        
        # Reversing sublists isn't needed if we just attach second_part before first_part:
        tail = second_part
        while tail.next:
            tail = tail.next
        tail.next = first_part
        
        return second_part
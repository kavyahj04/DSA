class Solution:
    def addOne(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return ListNode(1)
            
        # Step 1: Reverse the linked list
        prev = None
        curr = head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # 'prev' is now the new head of the reversed list
        reversed_head = prev 
        
        # Step 2: Add one with carry logic
        curr = reversed_head
        carry = 1
        
        while curr:
            total = curr.val + carry
            curr.val = total % 10
            carry = total // 10
            
            # If we are at the last node and still have a carry, 
            # append a new node and break out
            if not curr.next and carry:
                curr.next = ListNode(carry)
                carry = 0
                
            curr = curr.next
            
        # Step 3: Reverse the list back to its original order
        prev = None
        curr = reversed_head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
            
        return prev  # 'prev' is now the head of the final modified list

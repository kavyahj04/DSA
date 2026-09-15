class ListNode():
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next
    
    def sort_list(self, head:ListNode) -> ListNode:

        # 1. Create dummy heads to anchor the start of each list
        zero_dummy = ListNode()
        one_dummy = ListNode()
        two_dummy = ListNode()

        # 2. Create moving pointers initialized at the dummies
        zero = zero_dummy
        one = one_dummy
        two = two_dummy

        curr = head
        while curr:
            if curr.val == 0:
                zero.next = curr
                zero = zero.next
            elif curr.val == 1:
                one.next = curr
                one = one.next
            else:
                two.next = curr
                two = two.next
            curr = curr.next
        two.next = None
        zero.next = one_dummy.next if one_dummy.next else two_dummy.next
        one.next = two_dummy.next
    return zero_dummy.next
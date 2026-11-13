''' Structure of Linked List Node
class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None
        
'''
class Solution:
    def flatten(self, head):
        # code here
        def merge(list1, list2):
            dummy = Node(0)
            tail = dummy
            while list1 and list2:
                if list1.data <= list2.data:
                    tail.bottom = list1
                    list1 = list1.bottom
                else:
                    tail.bottom = list2
                    list2 = list2.bottom
                tail = tail.bottom
                tail.next = None
            if list1:
                tail.bottom = list1
            else:
                tail.bottom = list2
            return dummy.bottom
        if not head or not head.next:
            return head
        flattened_right = self.flatten(head.next)
        return merge(head, flattened_right)
# Representation 

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None      # reference to left child Node (or None)
        self.right = None     # reference to right child Node (or None)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

# root ──► [1 | left | right]
#                 │      └──► [3 | None | None]
#                 └──► [2 | left | right]
#                           │      └──► [5 | None | None]
#                           └──► [4 | None | None]

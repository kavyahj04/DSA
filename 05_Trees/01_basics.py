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

# DFS 

# 1. Preorder (Root → Left → Right)

def preorder(node, out):
    if node is None:
        return
    out.append(node.val)      # process BEFORE going down
    preorder(node.left, out)
    preorder(node.right, out)
    return out

print(preorder(root, []))   # [1, 2, 4, 5, 3]

# 2. Inorder (Left → Root → Right)

def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)      # process BETWEEN the two calls
    inorder(node.right, out)
    return out

print(inorder(root, []))    # [4, 2, 5, 1, 3]


# 3. Postorder (Left → Right → Root)

def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)      # process AFTER both children
    return out

print(postorder(root, []))  # [4, 5, 2, 3, 1]

# BFS - Level order traversal

from collections import deque

def level_order_flat(root):
    if root is None:
        return []
    out = []
    q = deque([root])
    while q:
        node = q.popleft()          # O(1); list.pop(0) is O(n), avoid it
        out.append(node.val)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return out

print(level_order_flat(root))   # [1, 2, 3, 4, 5]

# ITERATIVE 

# 1. Iterative Preorder (easy)

def preorder_iter(root):
    if root is None:
        return []
    out, stack = [], [root]
    while stack:
        node = stack.pop()
        out.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return out

print(preorder_iter(root))   # [1, 2, 4, 5, 3]


# 2 Iterative Inorder

def postorder_iter_2stack(root):
    if root is None:
        return []
    s1, s2 = [root], []
    while s1:
        node = s1.pop()
        s2.append(node.val)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    return s2[::-1]

print(postorder_iter_2stack(root))   # [4, 5, 2, 3, 1]

# 3 Iterative Postorder, two-stack version

def postorder_iter_2stack(root):
    if root is None:
        return []
    s1, s2 = [root], []
    while s1:
        node = s1.pop()
        s2.append(node.val)
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
    return s2[::-1]

print(postorder_iter_2stack(root))   # [4, 5, 2, 3, 1]

# 4. Iterative Postorder, one-stack version

def postorder_iter_1stack(root):
    out, stack = [], []
    curr, last = root, None
    while curr or stack:
        if curr:
            stack.append(curr)
            curr = curr.left
        else:
            peek = stack[-1]
            if peek.right and last is not peek.right:
                curr = peek.right
            else:
                out.append(peek.val)
                last = stack.pop()
    return out

print(postorder_iter_1stack(root))   # [4, 5, 2, 3, 1]
# Iterative Preorder (easy)

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

# Iterative Inorder

def inorder_iter(root):
    out, stack = [], []
    curr = root
    while curr or stack:
        while curr:
            stack.append(curr)
            curr = curr.left
        curr = stack.pop()
        out.append(curr.val)
        curr = curr.right
    return out

print(inorder_iter(root))    # [4, 2, 5, 1, 3]

# Iterative Postorder,

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


# Iterative Postorder, one-stack version

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
# Preorder (Root → Left → Right)

def preorder(node, out):
    if node is None:
        return
    out.append(node.val)      # process BEFORE going down
    preorder(node.left, out)
    preorder(node.right, out)
    return out

print(preorder(root, []))   # [1, 2, 4, 5, 3]


# Inorder (Left → Root → Right)

def inorder(node, out):
    if node is None:
        return
    inorder(node.left, out)
    out.append(node.val)      # process BETWEEN the two calls
    inorder(node.right, out)
    return out

print(inorder(root, []))    # [4, 2, 5, 1, 3]


# Postorder (Left → Right → Root)

def postorder(node, out):
    if node is None:
        return
    postorder(node.left, out)
    postorder(node.right, out)
    out.append(node.val)      # process AFTER both children
    return out

print(postorder(root, []))  # [4, 5, 2, 3, 1]
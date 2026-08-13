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
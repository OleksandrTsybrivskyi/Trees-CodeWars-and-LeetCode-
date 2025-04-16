from collections import deque
def tree_by_levels(node):
    if node is None:
        return []
    q = deque()
    ans = []
    q.append(node)
    while q:
        node = q.popleft()
        ans.append(node.value)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return ans

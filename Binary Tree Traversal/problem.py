# Pre-order traversal
def pre_order(node):
    if node is None:
        return []
    ans = []
    ans.append(node.data)
    if node.left:
        ans.extend(pre_order(node.left))
    if node.right:
        ans.extend(pre_order(node.right))
    return ans

# In-order traversal
def in_order(node):
    if node is None:
        return []
    ans = []
    if node.left:
        ans.extend(in_order(node.left))
    ans.append(node.data)
    if node.right:
        ans.extend(in_order(node.right))
    return ans

# Post-order traversal
def post_order(node):
    if node is None:
        return []
    ans = []
    if node.left:
        ans.extend(post_order(node.left))
    if node.right:
        ans.extend(post_order(node.right))
    ans.append(node.data)
    return ans

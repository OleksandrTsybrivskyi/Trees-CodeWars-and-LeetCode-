# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        root_of_the_root = TreeNode(val = None, left = root, right = None)
        node = root
        prev = root_of_the_root
        prev_come_from = 'left'
        while node != None and node.val != key:
            if node.val < key:
                prev = node
                node = node.right
                prev_come_from = 'right'
            else:
                prev = node
                node = node.left
                prev_come_from = 'left'
        if node is None:
            return root_of_the_root.left
        if node.left is None and node.right is None:
            if prev_come_from == 'left':
                prev.left = None
            else:
                prev.right = None
        elif node.left is None:
            if prev_come_from == 'left':
                prev.left = node.right
            else:
                prev.right = node.right
        elif node.right is None:
            if prev_come_from == 'left':
                prev.left = node.left
            else:
                prev.right = node.left
        else:
            checkpoint_node = node
            checkpoint_prev = prev
            checkpoint_prev_come_from = prev_come_from
            prev_come_from = 'left'
            prev = node
            node = node.left
            while node.right is not None:
                prev = node
                node = node.right
                prev_come_from = 'right'
            if prev_come_from == 'left':
                prev.left = node.left
            else:
                prev.right = node.left
            node.left = checkpoint_node.left
            node.right = checkpoint_node.right
            if checkpoint_prev_come_from == 'left':
                checkpoint_prev.left = node
            else:
                checkpoint_prev.right = node
        return root_of_the_root.left
        
            


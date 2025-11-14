# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # i think we have to consider possible different scenarios first
        def dfs(node, target, path):
            if not node:
                return None
            
            path.append(node)
            
            if node == target:
                return path
            
            next_node = node.left if target.val < node.val else node.right
            return dfs(next_node, target, path)

            return [node] + path

        p_traversal = dfs(root, p, [])
        q_traversal = dfs(root, q, [])
        prev = root
        for path1, path2 in zip(p_traversal, q_traversal):
            if path1 != path2:
                return prev
            prev = path1
        return prev
        
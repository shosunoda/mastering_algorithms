# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # so in this question, we defined good node 
        # if there are no values greater than x on the the way from root to node
        # this just means we have to mainta a max value that we need to pass on, and if its greater than, just + 1
        def dfs(node, highest):
            if node is None:
                return 0
            count = 1
            if highest > node.val:
                count = 0
            highest = max(highest, node.val)
            return count + dfs(node.left,highest) + dfs(node.right, highest)

        return dfs(root, root.val - 1)
        
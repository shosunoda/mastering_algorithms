# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # basically, we want to swith its branches at every single point, what happens when we reach a null branch, dont think it mattes 
        # so we want to try and swap the branches at each level 
        # this from the dounds of it looks like recursion 
        # root.left = root .right
        # swapbranch(root.left)
        #sawpbranch(root.right)
        # if its null, we start returning
        def swapbranch(node):
            if node is None:
                return 
            node.left, node.right = node.right, node.left
            swapbranch(node.left)
            swapbranch(node.right)
            return
        swapbranch(root)
        return root

        
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # wea given a binary tree and we have to determine if its a valid binary search tre
        # and the poerties of binary search tree ias as follows 
        # all nods to the left should ble smaller than the root node, and all nodes to the right should be greater than the root node 
        # i think a clarifying to be be asked does this containt discint values
        # another thing is so to make sure is. valid bst, we we want to make sure we look at the left, then the root, then rhe right
        # and we do this for every subtree 
        #i mean this creams recursion to me, the probelm I face with this question speciciflcally is how do we pass on the number it should be larger than 
        # ok so once we recurse all the way to the bottom of the binary tree 
        # we then want to stoore the value that have stores, and check that is smaller than all othe rvalues after it sees right
        # because we are processing from leftwards 
        # yeah thats the pronlem I face
        # also this is cleary dfs because we want to reach the bottom of the tree first and then do comparisons tarting there 
        # i mean if we cant gguarntere comparisons down there, i think another aroundabout solution is to store the values 
        # in the right way and then fter storing the values, we can actually confirm if they in the requires order
        if root is None:
            return True
        def dfs(node, high, low):
            if node is None:
                return True
            if not(node.val < high and node.val > low):
                return False
            return dfs(node.left, node.val, low) and dfs(node.right, high, node.val)

        return dfs(root, float('inf'), - float('inf'))
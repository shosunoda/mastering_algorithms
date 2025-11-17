from collections import deque
from typing import Optional, List   
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # i think at every level, we try and process ndoes from the right hand side
        # and add it to ur result
        # if theres no right node, we unfortunately process the left node
        # but once again this looks to be bfs again
        # 
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            for i in range(len(queue)):
                cur_node = queue.popleft()
                if i == 0:
                    result.append(cur_node.val)
                if cur_node.right:
                        queue.append(cur_node.right)
                if cur_node.left:
                    queue.append(cur_node.left)
        return result


        
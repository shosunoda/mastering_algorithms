from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # so weant to process things by level from the left, 
        # i think the best way to do is this to just add a bias to process nodes from the left first
        # now the problem is when we go throgh levels
        # how do ensure theres a slot for it 
        # also, idealistically the best way to do this through bfs i just realised
        # since we are doing level traversal 
        # how would do do that
        #
        result = []
        if root is None:
            return []
        queue = deque()
        queue.append(root)
        while queue:
            cur_level = []
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                cur_level.append(cur_node.val)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(cur_level)
        return result

        
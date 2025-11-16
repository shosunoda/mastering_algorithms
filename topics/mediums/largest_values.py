from collections import deque
from typing import Optional, List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# wwe will two variabels passed in the recrusve function, namely the node we are passing and the level in which we are at 
# we will have a base case in which if the node is None, that happens when we reach the end of the branch, we return
# if not, we will try and index into the result table at the index, and check its maximum
# i could do this using a map, to make things easier, however, i want to try do this with an array just to simplify the code
# 
# actually because its abinary search, tree, ad we are going to process through levels, a bfs approach may be warrwanted
# so lets try and do that instead
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            max_value = -float('inf')
            for _ in range(len(queue)):
                cur_node = queue.popleft()
                max_value = max(cur_node.val, max_value)
                if cur_node.left:
                    queue.append(cur_node.left)
                if cur_node.right:
                    queue.append(cur_node.right)
            result.append(max_value)
        return result

        
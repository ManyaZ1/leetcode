# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: return True
        elif not p or not q: return False
        if p.val != q.val:return False

        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#loop

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = deque([(p, q)])  # Use a stack to hold pairs of nodes
        
        while stack:
            node1, node2 = stack.popleft()
            
            # If both are None, continue checking other nodes
            if not node1 and not node2:
                continue
            
            # If one is None and the other isn't, or their values differ
            if not node1 or not node2 or node1.val != node2.val:
                return False
            
            # Add left and right children pairs to the stack for further comparison
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        
        return True  # All nodes were the same

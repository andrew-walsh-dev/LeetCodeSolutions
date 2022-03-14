# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        #node is null, return None
        if not root:
            return None
            
        #recursive call to traverse tree
        child_left = self.lowestCommonAncestor(root.left, p, q)
        child_right = self.lowestCommonAncestor(root.right, p, q)
        
        #if both sides returned something, return the node
        if child_left and child_right:
            return root
        
        #if node contains p or q, return the node
        if root == p or root == q:
            return root
        
        #if only one side returns something, return that side
        if child_left or child_right:
            return child_left or child_right
        
        return None
            
            
        
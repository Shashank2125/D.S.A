# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: Optional[TreeNode]
        :type root2: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(root,leaf):
            if root.left is None and root.right is None:
                leaf.append(root.val)
            if root.left:
                dfs(root.left,leaf)
            if root.right:
                dfs(root.right,leaf)
        leaf1=[]
        leaf2=[]
        dfs(root1,leaf1)
        dfs(root2,leaf2)
        return leaf1==leaf2
            

        
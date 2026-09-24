# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        def dfs(node,maxx):
            if node is None:
                return 0
            count=0
            if node.val>=maxx:
                count=1
            maxx=max(maxx,node.val)
            count+=dfs(node.right,maxx)
            count+=dfs(node.left,maxx)
            return count
        return dfs(root,root.val)
            


        
        
        
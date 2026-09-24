# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        if root is None:
            return 0
        def summ(node,targetSum):
            if node is None:
                return 0
            count=0
            if node.val==targetSum:
                count+=1
            count+=summ(node.left,targetSum-node.val)
            count+=summ(node.right,targetSum-node.val)
            return count
        count=summ(root,targetSum)
        #counting can start from any node from the deep of the tree also
        count+=self.pathSum(root.left,targetSum)
        count+=self.pathSum(root.right,targetSum)
        return count
        
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def longestZigZag(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root is None:
            return 0
        direction=0
        length=0
        def zigzag(node,direction,length):
            if node is None:
                return length-1
            if direction==0:
                return max(
                zigzag(node.right,1,length+1),
                zigzag(node.left,0,1))
            else:
                return max(
                zigzag(node.left,0,length+1),
                zigzag(node.right,1,1))
        return zigzag(root,direction,length)
        

            
        